from django.db import models


class Equipment(models.Model):
    # Equipment Choices
    MASK = 'MSK'
    GOWN = 'GWN'
    GOGGLE = 'GOG'
    CAP = 'CPS'
    ITEM_NAME_CHOICES = [
        (MASK, 'Mask'),
        (GOWN, 'Gown'),
        (GOGGLE, 'Goggle'),
        (CAP, 'Cap'),
    ]


    # Condition Choices
    GOOD = 'GOOD'
    BAD = 'BAD'
    CONDITION_CHOICES = [
        (GOOD, 'Good'),
        (BAD, 'Bad'),
    ]


    # Supplier Choices
    LGU = 'LG'
    DONATION = 'DN'
    SUPPLIER_CHOICES = [
        (LGU, 'Local Government Unit'),
        (DONATION, 'Donation'),
    ]


    package_number = models.CharField(max_length=200, unique=True)
    item_name = models.CharField(
                    max_length=3,
                    choices=ITEM_NAME_CHOICES,
                    default=MASK,
                    )
    qty_per_package = models.IntegerField()
    condition_upon_received = models.CharField(
                    max_length=6,
                    choices=CONDITION_CHOICES,
                    default=GOOD,
                    )
    supplier = models.CharField(
                    max_length=2,
                    choices=SUPPLIER_CHOICES,
                    default=LGU,
                    )
    received_by = models.CharField(max_length=200)
    checked_by = models.CharField(max_length=200)
    date_of_receipt = models.DateField()


    def __str__(self):
        return f'{self.package_number} {self.item_name}'


class Used(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_being_used = models.DateField()
    qty_to_be_used = models.IntegerField()
    is_used = models.BooleanField(default=True)



    def __str__(self):
        return self.qty_to_be_used



class Disposed(models.Model):
    used = models.ForeignKey(Used, on_delete=models.CASCADE, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_disposed = models.DateField(auto_now_add=True)
    qty_to_be_disposed = models.IntegerField()


    def __str__(self):
        return self.qty_to_be_disposed