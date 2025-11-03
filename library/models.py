from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    membership_date = models.DateField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    year_published = models.IntegerField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, through='BookAuthor')

    def __str__(self):
        return self.title

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'author')

class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    books = models.ManyToManyField(Book, through='LoanDetail')

    def __str__(self):
        return f"Loan {self.id} by {self.member.name}"

class LoanDetail(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('loan', 'book')