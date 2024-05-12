from picks.models import orderLines, orders, productMaster
import csv

orderlines = [
  {
    "id": 1,
    "order_number": {
      "order_number": "ORD0030",
      "customer_name": "Olivia Taylor",
      "order_date": "2023-04-20"
    },
    "sku": {
      "sku": 766734,
      "title": "Chicken",
      "location_id": "S62T",
      "on_hand": 63
    },
    "pick_id": 1040,
    "location_id": "S62T",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 2,
    "order_number": {
      "order_number": "ORD0030",
      "customer_name": "Olivia Taylor",
      "order_date": "2023-04-20"
    },
    "sku": {
      "sku": 627926,
      "title": "Tofu",
      "location_id": "6CD6",
      "on_hand": 8
    },
    "pick_id": 1039,
    "location_id": "6CD6",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 3,
    "order_number": {
      "order_number": "ORD0029",
      "customer_name": "Liam Hernandez",
      "order_date": "2023-04-19"
    },
    "sku": {
      "sku": 825955,
      "title": "Pizza",
      "location_id": "1F6W",
      "on_hand": 75
    },
    "pick_id": 1038,
    "location_id": "1F6W",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 4,
    "order_number": {
      "order_number": "ORD0029",
      "customer_name": "Liam Hernandez",
      "order_date": "2023-04-19"
    },
    "sku": {
      "sku": 825955,
      "title": "Pizza",
      "location_id": "1F6W",
      "on_hand": 75
    },
    "pick_id": 1037,
    "location_id": "1F6W",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 5,
    "order_number": {
      "order_number": "ORD0028",
      "customer_name": "Ava Miller",
      "order_date": "2023-04-23"
    },
    "sku": {
      "sku": 921319,
      "title": "Curry",
      "location_id": "B2UP",
      "on_hand": 39
    },
    "pick_id": 1036,
    "location_id": "B2UP",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 6,
    "order_number": {
      "order_number": "ORD0028",
      "customer_name": "Ava Miller",
      "order_date": "2023-04-23"
    },
    "sku": {
      "sku": 399497,
      "title": "Fajitas",
      "location_id": "ZFMX",
      "on_hand": 42
    },
    "pick_id": 1035,
    "location_id": "ZFMX",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 7,
    "order_number": {
      "order_number": "ORD0028",
      "customer_name": "Ava Miller",
      "order_date": "2023-04-23"
    },
    "sku": {
      "sku": 399497,
      "title": "Fajitas",
      "location_id": "ZFMX",
      "on_hand": 42
    },
    "pick_id": 1034,
    "location_id": "ZFMX",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 8,
    "order_number": {
      "order_number": "ORD0027",
      "customer_name": "Noah Johnson",
      "order_date": "2023-04-21"
    },
    "sku": {
      "sku": 777462,
      "title": "Lamb",
      "location_id": "KZS5",
      "on_hand": 17
    },
    "pick_id": 1033,
    "location_id": "KZS5",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 9,
    "order_number": {
      "order_number": "ORD0027",
      "customer_name": "Noah Johnson",
      "order_date": "2023-04-21"
    },
    "sku": {
      "sku": 777462,
      "title": "Lamb",
      "location_id": "KZS5",
      "on_hand": 17
    },
    "pick_id": 1032,
    "location_id": "KZS5",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 10,
    "order_number": {
      "order_number": "ORD0026",
      "customer_name": "Sophia Williams",
      "order_date": "2023-04-22"
    },
    "sku": {
      "sku": 766734,
      "title": "Chicken",
      "location_id": "S62T",
      "on_hand": 63
    },
    "pick_id": 1031,
    "location_id": "S62T",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 11,
    "order_number": {
      "order_number": "ORD0026",
      "customer_name": "Sophia Williams",
      "order_date": "2023-04-22"
    },
    "sku": {
      "sku": 997580,
      "title": "Steak",
      "location_id": "9PL1",
      "on_hand": 67
    },
    "pick_id": 1030,
    "location_id": "9PL1",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 12,
    "order_number": {
      "order_number": "ORD0025",
      "customer_name": "Emily Hall",
      "order_date": "2023-03-20"
    },
    "sku": {
      "sku": 512239,
      "title": "Hotdog",
      "location_id": "5U67",
      "on_hand": 59
    },
    "pick_id": 1029,
    "location_id": "5U67",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 13,
    "order_number": {
      "order_number": "ORD0025",
      "customer_name": "Emily Hall",
      "order_date": "2023-03-20"
    },
    "sku": {
      "sku": 825955,
      "title": "Pizza",
      "location_id": "1F6W",
      "on_hand": 75
    },
    "pick_id": 1028,
    "location_id": "1F6W",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 14,
    "order_number": {
      "order_number": "ORD0004",
      "customer_name": "Chris Lee",
      "order_date": "2023-04-13"
    },
    "sku": {
      "sku": 945658,
      "title": "Vegan",
      "location_id": "9O67",
      "on_hand": 12
    },
    "pick_id": 1027,
    "location_id": "9O67",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 15,
    "order_number": {
      "order_number": "ORD0020",
      "customer_name": "Michael Gonzalez",
      "order_date": "2023-04-08"
    },
    "sku": {
      "sku": 825955,
      "title": "Pizza",
      "location_id": "1F6W",
      "on_hand": 75
    },
    "pick_id": 1026,
    "location_id": "1F6W",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 16,
    "order_number": {
      "order_number": "ORD0014",
      "customer_name": "Charlotte Nelson",
      "order_date": "2023-03-05"
    },
    "sku": {
      "sku": 270068,
      "title": "Dumplings",
      "location_id": "JV2J",
      "on_hand": 74
    },
    "pick_id": 1025,
    "location_id": "JV2J",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 17,
    "order_number": {
      "order_number": "ORD0012",
      "customer_name": "Ella Garcia",
      "order_date": "2023-03-10"
    },
    "sku": {
      "sku": 314507,
      "title": "Wings",
      "location_id": "D8P7",
      "on_hand": 52
    },
    "pick_id": 1024,
    "location_id": "D8P7",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 18,
    "order_number": {
      "order_number": "ORD0009",
      "customer_name": "John Doe",
      "order_date": "2023-04-03"
    },
    "sku": {
      "sku": 692071,
      "title": "Salad",
      "location_id": "08AC",
      "on_hand": 75
    },
    "pick_id": 1023,
    "location_id": "08AC",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 19,
    "order_number": {
      "order_number": "ORD0005",
      "customer_name": "Ethan Brown",
      "order_date": "2023-03-11"
    },
    "sku": {
      "sku": 921319,
      "title": "Curry",
      "location_id": "B2UP",
      "on_hand": 39
    },
    "pick_id": 1022,
    "location_id": "B2UP",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 20,
    "order_number": {
      "order_number": "ORD0003",
      "customer_name": "Chris Lee",
      "order_date": "2023-04-05"
    },
    "sku": {
      "sku": 766734,
      "title": "Chicken",
      "location_id": "S62T",
      "on_hand": 63
    },
    "pick_id": 1021,
    "location_id": "S62T",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 21,
    "order_number": {
      "order_number": "ORD0014",
      "customer_name": "Charlotte Nelson",
      "order_date": "2023-03-05"
    },
    "sku": {
      "sku": 825955,
      "title": "Pizza",
      "location_id": "1F6W",
      "on_hand": 75
    },
    "pick_id": 1010,
    "location_id": "1F6W",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 22,
    "order_number": {
      "order_number": "ORD0005",
      "customer_name": "Ethan Brown",
      "order_date": "2023-03-11"
    },
    "sku": {
      "sku": 766734,
      "title": "Chicken",
      "location_id": "S62T",
      "on_hand": 63
    },
    "pick_id": 1008,
    "location_id": "S62T",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 23,
    "order_number": {
      "order_number": "ORD0020",
      "customer_name": "Michael Gonzalez",
      "order_date": "2023-04-08"
    },
    "sku": {
      "sku": 997580,
      "title": "Steak",
      "location_id": "9PL1",
      "on_hand": 67
    },
    "pick_id": 1007,
    "location_id": "9PL1",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 24,
    "order_number": {
      "order_number": "ORD0003",
      "customer_name": "Chris Lee",
      "order_date": "2023-04-05"
    },
    "sku": {
      "sku": 270068,
      "title": "Dumplings",
      "location_id": "JV2J",
      "on_hand": 74
    },
    "pick_id": 1006,
    "location_id": "JV2J",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 25,
    "order_number": {
      "order_number": "ORD0024",
      "customer_name": "Amelia Evans",
      "order_date": "2023-04-08"
    },
    "sku": {
      "sku": 270068,
      "title": "Dumplings",
      "location_id": "JV2J",
      "on_hand": 74
    },
    "pick_id": 1005,
    "location_id": "JV2J",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 26,
    "order_number": {
      "order_number": "ORD0020",
      "customer_name": "Michael Gonzalez",
      "order_date": "2023-04-08"
    },
    "sku": {
      "sku": 512239,
      "title": "Hotdog",
      "location_id": "5U67",
      "on_hand": 59
    },
    "pick_id": 1004,
    "location_id": "5U67",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 27,
    "order_number": {
      "order_number": "ORD0012",
      "customer_name": "Ella Garcia",
      "order_date": "2023-03-10"
    },
    "sku": {
      "sku": 766734,
      "title": "Chicken",
      "location_id": "S62T",
      "on_hand": 63
    },
    "pick_id": 1003,
    "location_id": "S62T",
    "pick_quantity": 3,
    "pick_status": "pending"
  },
  {
    "id": 28,
    "order_number": {
      "order_number": "ORD0009",
      "customer_name": "John Doe",
      "order_date": "2023-04-03"
    },
    "sku": {
      "sku": 825955,
      "title": "Pizza",
      "location_id": "1F6W",
      "on_hand": 75
    },
    "pick_id": 1002,
    "location_id": "1F6W",
    "pick_quantity": 1,
    "pick_status": "pending"
  },
  {
    "id": 29,
    "order_number": {
      "order_number": "ORD0003",
      "customer_name": "Chris Lee",
      "order_date": "2023-04-05"
    },
    "sku": {
      "sku": 997580,
      "title": "Steak",
      "location_id": "9PL1",
      "on_hand": 67
    },
    "pick_id": 1001,
    "location_id": "9PL1",
    "pick_quantity": 2,
    "pick_status": "pending"
  },
  {
    "id": 30,
    "order_number": {
      "order_number": "ORD0005",
      "customer_name": "Ethan Brown",
      "order_date": "2023-03-11"
    },
    "sku": {
      "sku": 512239,
      "title": "Hotdog",
      "location_id": "5U67",
      "on_hand": 59
    },
    "pick_id": 1002,
    "location_id": "5U67",
    "pick_quantity": 2,
    "pick_status": "pending"
  }
]

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

    for obj in orderlines:
        sku_ = productMaster(
            sku= obj['sku']['sku'],
            title= obj['sku']['title'],  
            location_id=obj['sku']['location_id'] , 
            on_hand= obj['sku']['on_hand'] )
        
        ordernumber_ = orders(
            order_number = obj['order_number']['order_number'],
            customer_name = obj['order_number']['customer_name'],
            order_date = obj['order_number']['order_date']
        )
        # print(obj["pick_id"])
        orderlines_tosave = orderLines(
            pick_id = obj['pick_id'],
            order_number = ordernumber_,
            sku = sku_,
            location_id = obj['location_id'],
            pick_quantity = obj['pick_quantity']
            )
        orderlines_tosave.save()
 