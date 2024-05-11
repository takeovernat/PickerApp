from picks.models import orderLines, orders, productMaster
import csv


def run():
   
    with open('testdata/Orders.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        orders.objects.all().delete()
        for row in reader:
            print(row)

            orders_local = orders(
                        order_number=row[0],
                        customer_name=row[1],
                        order_date=row[2]
                        )
            orders_local.save()

    with open('testdata/ProductMaster.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        productMaster.objects.all().delete()
        for row in reader:
            print(row)

            productmaster = productMaster(
                        sku=row[0],
                        title=row[1],
                        location_id=row[2],
                        on_hand = row[3]
                        )
            productmaster.save()

 # with open('testdata/OrderLines.csv') as file:
    #     reader = csv.reader(file)
    #     next(reader)  # Advance past the header

    #     orderLines.objects.all().delete()
    #     for row in reader:
    #         print(row)

    #         orderlines = orderLines(
    #                     pick_id=row[0],
    #                     order_number=row[1],
    #                     sku=row[2],
    #                     location_id = row[3],
    #                     pick_quantity = row[4]
    #                     )
    #         orderlines.save()

        

       