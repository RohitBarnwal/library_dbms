
### Core Architectural Approach

*   **Service Layer (Abstraction & SRP):** For each core domain entity (`Book`, `Member`, `Loan`), we will create a dedicated service class (e.g., `BookService`, `LoanService`). This service will encapsulate all business logic related to that entity, providing a clear API to the rest of the application (like Django views or API endpoints). This adheres to the **Single Responsibility Principle (SRP)**.
*   **Dependency Injection (DI & Test-Friendly):** Services will not be instantiated directly within views. Instead, they will be injected, allowing for easy mocking and testing. This makes the entire structure **test-friendly** and adheres to the **Dependency Inversion Principle (DIP)**.
*   **Event-Driven Design (Decoupling & Open/Closed Principle):** For key business processes, services will publish events instead of directly calling other services. For example, when a loan is created, the `LoanService` will publish a `BookLoaned` event. Other parts of the system (like a `NotificationService` or `AnalyticsService`) can subscribe to this event without the `LoanService` needing to know about them. This creates a highly decoupled system and adheres to the **Open/Closed Principle (OCP)**, as we can add new event listeners without modifying the original service.

---

### EPICs and Features

Here are the EPICs and their corresponding features:

### **EPIC-01: Library Catalog Management**

This epic covers all functionality related to the management of the library's physical and digital assets, including books, authors, and publishers.

*   **Feature 1.1: Add a New Book to the Catalog**
    *   **Description:** As a librarian, I want to add a new book with its complete details (title, ISBN, authors, publisher, etc.) so that it becomes part of the library's discoverable inventory.
    *   **Technical Implementation & Best Practices:**
        *   An API endpoint (`POST /api/books/`) will accept the new book's data.
        *   The view/controller will call `BookService.add_book(data)`.
        *   The `BookService` will encapsulate the logic to:
            1.  Validate the incoming data.
            2.  Find or create the associated `Author` and `Publisher` records.
            3.  Create the `Book` and `BookAuthor` records within a database transaction to ensure atomicity.
        *   Upon successful creation, the `BookService` will publish a `NewBookAdded` event containing the book's ID and details. This allows other services (e.g., a search indexer) to react.

*   **Feature 1.2: Manage Author & Publisher Information**
    *   **Description:** As a librarian, I need to be able to create, view, update, and delete records for authors and publishers to keep the catalog's metadata accurate.
    *   **Technical Implementation & Best Practices:**
        *   Dedicated `AuthorService` and `PublisherService` will handle all CRUD (Create, Read, Update, Delete) logic for their respective entities.
        *   This separation ensures each service has a single responsibility (SRP).
        *   API endpoints (e.g., `POST /api/authors/`, `PUT /api/authors/{id}/`) will be thin layers that delegate directly to these services.

### **EPIC-02: Patron & Staff Management**

This epic focuses on the people interacting with the library system, including members (patrons) and staff.

*   **Feature 2.1: Register a New Library Member**
    *   **Description:** As a librarian, I want to register a new member by entering their personal details so they can borrow books.
    *   **Technical Implementation & Best Practices:**
        *   A `MemberService` will have a `register_member(name, email, ...)` method.
        *   This service will encapsulate all validation, such as checking for a unique email address.
        *   After successfully creating the `Member` record, the service will publish a `MemberRegistered` event.
        *   A separate `NotificationService` will listen for the `MemberRegistered` event and trigger a welcome email to the new member. This is a perfect example of event-driven decoupling.

### **EPIC-03: Book Circulation Management**

This is the core operational epic, handling the entire lifecycle of borrowing and returning books.

*   **Feature 3.1: Issue Books to a Member (Create a Loan)**
    *   **Description:** As a librarian, I want to process a loan for a member by scanning one or more books, so their borrowing activity is officially tracked.
    *   **Technical Implementation & Best Practices:**
        *   A `LoanService` will expose a `create_loan(member_id, book_ids, staff_id)` method.
        *   This method is a critical transaction and will encapsulate the entire process:
            1.  Verify the `member_id` is valid.
            2.  Check the availability of each book in `book_ids` (i.e., not already on loan).
            3.  Calculate the `due_date`.
            4.  Create the `Loan` and `LoanDetail` records within a single database transaction.
        *   If successful, the service will publish a `BooksLoaned` event with the loan details. This event can be used by other services to, for example, update an analytics dashboard.

*   **Feature 3.2: Process the Return of Books**
    *   **Description:** As a librarian, I want to mark a loan's books as returned, calculate any applicable fines, and make the books available again.
    *   **Technical Implementation & Best Practices:**
        *   The `LoanService` will have a `return_books(loan_id, book_ids)` method.
        *   The business logic will:
            1.  Update the `return_date` on the `Loan` record.
            2.  Use a separate, injected `FineCalculationStrategy` to determine if a fine is owed based on `due_date` vs. `return_date`. This makes the fine logic swappable (OCP).
            3.  Update the `fine` amount on the `Loan` record.
        *   The service will then publish a `BooksReturned` event.

*   **Feature 3.3: Daily Overdue Loan Processing**
    *   **Description:** As an automated system process, I want to identify all overdue loans daily and trigger notifications.
    *   **Technical Implementation & Best Practices:**
        *   A scheduled background task (e.g., a Celery task or cron job) will run once a day.
        *   The task will call `LoanService.process_overdue_loans()`.
        *   This service method finds all loans where `due_date` is in the past and `return_date` is null.
        *   For each overdue loan found, it will publish a `LoanOverdue` event containing the `loan_id` and `member_id`.
        *   The `NotificationService` will listen for `LoanOverdue` events and send reminder emails to the relevant members, completely decoupled from the loan processing logic.
