from django.db import models

# Create your models here.

class productMaster(models.Model):
    sku = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    location_id = models.CharField(max_length=120)
    on_hand = models.IntegerField()

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.sku, self.title, self.location_id, self.on_hand)

class orders(models.Model):
    order_number = models.CharField(max_length=120, primary_key=True)
    customer_name = models.CharField(max_length=120)
    order_date = models.DateField()

    class Meta:
        get_latest_by = ['-order_date']

    def __str__(self):
        return "{0} {1} {2}".format(self.order_number, self.customer_name, self.order_date)

class orderLines(models.Model):
    pick_id = models.IntegerField()
    order_number = models.ForeignKey(orders, on_delete=models.CASCADE)
    sku = models.ForeignKey(productMaster, on_delete=models.CASCADE)
    location_id = models.CharField(max_length=120)
    pick_quantity = models.IntegerField()
    pick_status = models.CharField(max_length=120, default="pending")

    def __str__(self):
        return "{0} {1} {2}".format(self.pick_id, self.order_number, self.pick_quantity)

