# Business Requirements Document (BRD) for Library Database Management System

## 1. Introduction

### 1.1 Purpose

This document outlines the business requirements for a Library Database Management System. The system will automate and streamline the management of library resources, including books, members, and loans. It will provide a centralized database to track library assets, manage member information, and handle book borrowing and returning processes efficiently.

### 1.2 Scope

The scope of this project is to develop a web-based application that supports the core functions of a library. This includes:

*   **In Scope:**
    *   Managing the library's book collection.
    *   Managing member information.
    *   Tracking book loans, returns, and fines.
    *   Providing a search interface for books.
    *   Managing author and publisher information.
    *   User roles for staff and members.

*   **Out of Scope:**
    *   Integration with external systems (e.g., online payment gateways for fines).
    *   Advanced reporting and analytics features.
    *   Self-service features for members (e.g., online book reservations).

## 2. Business Process Overview

### 2.1 User Roles

The system will have two main user roles:

*   **Staff:** Library staff who will manage the system, including adding books, managing members, and processing loans.
*   **Member:** Library members who can borrow and return books.

### 2.2 High-Level Process Flow

1.  A member requests to borrow a book.
2.  A staff member checks the book's availability and the member's status.
3.  If the book is available and the member is in good standing, the staff member creates a loan record.
4.  The member returns the book on or before the due date.
5.  A staff member updates the loan record and checks for any fines.
6.  If there are fines, the member pays the amount, and the staff member updates the record.

## 3. Functional Requirements

### 3.1 User Management

*   **3.1.1:** The system shall allow authorized staff to add, edit, and delete staff user accounts.
*   **3.1.2:** Each staff user account shall have a unique username and a secure password.
*   **3.1.3:** The system shall differentiate between staff and member roles, with different levels of access and permissions.

### 3.2 Book Management

*   **3.2.1:** The system shall allow staff to add new books to the library's collection with details such as title, ISBN, year published, category, price, and publisher.
*   **3.2.2:** The system shall allow staff to edit and delete existing book records.
*   **3.2.3:** The system shall provide a search functionality to find books by title, author, or category.
*   **3.2.4:** The system shall track the availability of each book.

### 3.3 Author Management

*   **3.3.1:** The system shall allow staff to add, edit, and delete author records with details such as name, biography, and nationality.
*   **3.3.2:** The system shall support a many-to-many relationship between books and authors.

### 3.4 Publisher Management

*   **3.4.1:** The system shall allow staff to add, edit, and delete publisher records with details such as name, address, and contact number.
*   **3.4.2:** Each book shall be associated with one publisher.

### 3.5 Member Management

*   **3.5.1:** The system shall allow staff to register new members with details such as name, address, phone, email, and membership date.
*   **3.5.2:** The system shall allow staff to edit and delete member records.
*   **3.5.3:** Each member shall have a unique member ID.

### 3.6 Loan Management

*   **3.6.1:** The system shall allow staff to create a new loan record when a member borrows a book.
*   **3.6.2:** Each loan record shall include the book ID, member ID, staff ID, issue date, and due date.
*   **3.6.3:** The system shall allow staff to update a loan record when a book is returned.
*   **3.6.4:** The system shall calculate and apply fines for overdue books.
*   **3.6.5:** The system shall track the history of loans for each member and book.

## 4. Non-Functional Requirements

### 4.1 Performance

*   The system should be able to handle a moderate number of concurrent users without significant degradation in performance.
*   Search results should be displayed within a reasonable time frame (e.g., under 3 seconds).

### 4.2 Security

*   The system shall ensure that only authorized users can access the system's functionalities.
*   User passwords shall be stored securely (e.g., using hashing and salting).
*   The system shall be protected against common web vulnerabilities (e.g., SQL injection, cross-site scripting).

### 4.3 Usability

*   The user interface shall be intuitive and easy to use for both staff and members.
*   The system shall provide clear and informative messages to users.

### 4.4 Reliability

*   The system shall be available during the library's operating hours.
*   The system shall have a reliable backup and recovery mechanism to prevent data loss.

## 5. Data Requirements

### 5.1 Data Entities

The system will manage the following data entities:

*   **Member:** (Member_ID, Name, Address, Phone, Email, Membership_Date)
*   **Staff:** (Staff_ID, Name, Role, Phone, Email)
*   **Book:** (Book_ID, Title, ISBN, Year_Published, Category, Price, Publisher_ID)
*   **Author:** (Author_ID, Name, Biography, Nationality)
*   **Publisher:** (Publisher_ID, Name, Address, Contact_Number)
*   **Loan:** (Loan_ID, Member_ID, Staff_ID, Issue_Date, Due_Date, Return_Date, Fine)
*   **Loan_Details:** (Loan_ID, Book_ID)
*   **Book_Author:** (Book_ID, Author_ID)

### 5.2 Relationships

*   A **Member** can have multiple **Loans**.
*   A **Staff** member can process multiple **Loans**.
*   A **Book** can be part of multiple **Loan_Details**.
*   A **Publisher** can publish multiple **Books**.
*   A **Book** can have multiple **Authors**, and an **Author** can write multiple **Books**.
*   A **Loan** can have multiple **Loan_Details**.

## 6. Assumptions and Constraints

### 6.1 Assumptions

*   The library has a stable internet connection.
*   Staff members have basic computer literacy skills.

### 6.2 Constraints

*   The system will be developed using Python (Django) and a SQLite database.
*   The project has a limited budget and timeline.