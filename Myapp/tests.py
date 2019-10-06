from django.test import TestCase

# Create your tests here.
try:
    value=int(10.1)
    print(value)
except ValueError:
    print("This is not a whole number.")
