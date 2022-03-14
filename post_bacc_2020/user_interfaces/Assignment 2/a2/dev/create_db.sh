import sqlite3, csv

conn = sqlite3.connect("bikes.db")
c = conn.cursor()


sql = """
CREATE TABLE bikes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    wheels INTEGER,
    size INTEGER,
    motor INTEGER NOT NULL,
    folding INTEGER NOT NULL,
    image TEXT,
    available INTEGER
    );"""

c.execute(sql)
print("bikes database created")

c.execute("INSERT INTO bikes VALUES ('1','Sixthreezero Around The Block Womens Single Speed Cruiser Bicycle Coral w/ Black Seat/Grips','2','26','0','0','sixthreezero.jpg','2')")
c.execute("INSERT INTO bikes VALUES ('2','Roadmaster 26 Mens Granite Peak Mens Bike','2','26','0','0','roadmaster.jpg','0')")
c.execute("INSERT INTO bikes VALUES ('3','Fun 20 Inch Wheel Unicycle with Alloy Rim','1','20','0','0','unicycle.jpg','7')")
c.execute("INSERT INTO bikes VALUES ('4','Mongoose Dolomite Fat Tire Mountain Bike','2','26','0','0','mongoose.jpg','3')")
c.execute("INSERT INTO bikes VALUES ('5','EuroMini ZiZZO Campo 28lb Lightweight Aluminum Frame Shimano 7 - Speed Folding Bike','2','20','0','1','euromini.jpg','1')")
c.execute("INSERT INTO bikes VALUES ('6','Huffy Mountain Bike Summit Ridge w / Shimano & Trail Tires','2','24','0','0','huffy.jpg','0')")
c.execute("INSERT INTO bikes VALUES ('7','Razor RSF350 Electric Street Bike','2','10','1','0','razor.jpg','8')")
c.execute("INSERT INTO bikes VALUES ('8','Shaofu Folding Electric Bicycle – 350W 36V Waterproof E-Bike with 15 Mile Range Collapsible Frame and APP Speed Setting','2','12','1','1','shaofu.jpg','0')")
c.execute("INSERT INTO bikes VALUES ('9','Goplus Adult Tricycle Trike Cruise Bike Three-Wheeled Bicycle w/Large Size Basket for Recreation Shopping Exercise','3','26','0','0','tricycle.jpg','2')")
c.execute("INSERT INTO bikes VALUES ('10','Swagtron 200W SWAGCYCLE Envy Steel Frame Folding Electric Bicycle e Bike w / Automatic Headlight','2','12','1','1','swagtron.jpg','5')")

print("data added")
conn.commit()
conn.close()


