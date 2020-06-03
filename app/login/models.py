from django.db import models

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

class User(models.Model):
    """
        User Model
        Attributes:
        - First name
        - Last name
        - Email
        - Type of ID
        - ID (n_document)
        - Picture (Missed)
        - Department
        - City
        - Password (Encryptation missed)
    """

    first_name = models.CharField(max_length=32, blank=False, null=False)
    last_name = models.CharField(max_length=32, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True, validators=[validateEmail])
    type_id = models.CharField(max_length=2, blank=False, null=False)
    n_document = models.CharField(max_length=32, blank=False, null=False)
    department = models.CharField(max_length=32, blank=False, null=False)
    city = models.CharField(max_length=32, blank=False, null=False)
    password = models.CharField(max_length=32, blank=False, null=False)


    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Department(models.Model):
    """
        Department Model
        Attributtes:
        - Name
        - Code
    """
    name = models.CharField(max_length=32, blank=False, null=False)
    code = models.IntegerField(null=False)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})


class City(models.Model):
    """
        City Model

    """
    department = models.ForeignKey(Department,
                                   verbose_name=("department"),
                                   on_delete=models.CASCADE,
                                   null=True)
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=32, default="")

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("City_detail", kwargs={"pk": self.pk})
