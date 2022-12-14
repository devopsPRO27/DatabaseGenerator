import mysql.connector


class DBcon:

    def __init__(self, password):
        self.password = password

    def database_generator(self):
        # conn = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     password=self.password,
        # )
        # cursor = conn.cursor()
        # cursor.execute(f' CREATE DATABASE CurrencyDB')
        # cursor = conn.cursor()
        conn = mysql.connector.connect(
                 host='localhost',
                 user='root',
                 password=self.password,
                database='CurrencyDB'
             )
        cursor = conn.cursor()
        # cursor.execute(''' CREATE TABLE currencies (
        #                     currency_id VARCHAR(20)  PRIMARY KEY,
        #                     value FLOAT
        #         ) ''')
        cursor.execute('''
        INSERT INTO CurrencyDB.currencies VALUES
("USD",1),
  ("AED",3.6725),
  ("AFN",89.6941),
  ("ALL",114.2457),
  ("AMD",413.2282),
  ("ANG",1.7900),
  ("AOA",429.9365),
  ("ARS",129.0515),
  ("AUD",1.4426),
  ("AWG",1.7900),
  ("AZN",1.6941),
  ("BAM",1.9178),
  ("BBD",2.0000),
  ("BDT",93.4592),
  ("BGN",1.9179),
  ("BHD",0.3760),
  ("BIF",2027.9327),
  ("BMD",1.0000),
  ("BND",1.3858),
  ("BOB",6.8524),
  ("BRL",5.4809),
  ("BSD",1.0000),
  ("BTN",79.9633),
  ("BWP",12.7170),
  ("BYN",2.6863),
  ("BZD",2.0000),
  ("CAD",1.2878),
  ("CDF",1993.1721),
  ("CHF",0.9633),
  ("CLP",928.5443),
  ("CNY",6.7730),
  ("COP",4315.1567),
  ("CRC",678.5641),
  ("CUP",24.0000),
  ("CVE",108.1206),
  ("CZK",24.0521),
  ("DJF",177.7210),
  ("DKK",7.3153),
  ("DOP",54.2834),
  ("DZD",145.4306),
  ("EGP",18.9079),
  ("ERN",15.0000),
  ("ETB",51.8656),
  ("EUR",0.9806),
  ("FJD",2.2014),
  ("FKP",0.8353),
  ("FOK",7.3153),
  ("GBP",0.8353),
  ("GEL",2.7960),
  ("GGP",0.8353),
  ("GHS",8.4681),
  ("GIP",0.8353),
  ("GMD",54.1833),
  ("GNF",8647.1347),
  ("GTQ",7.7198),
  ("GYD",208.7159),
  ("HKD",7.8501),
  ("HNL",24.5204),
  ("HRK",7.3880),
  ("HTG",116.4171),
  ("HUF",388.7176),
  ("IDR",14976.9604),
  ("ILS",3.4311),
  ("IMP",0.8353),
  ("INR",79.9647),
  ("IQD",1456.1027),
  ("IRR",42049.3166),
  ("ISK",137.1455),
  ("JEP",0.8353),
  ("JMD",152.2543),
  ("JOD",0.7090),
  ("JPY",136.5949),
  ("KES",117.8399),
  ("KGS",80.3913),
  ("KHR",4076.8317),
  ("KID",1.4426),
  ("KMF",482.4003),
  ("KRW",1310.0574),
  ("KWD",0.2996),
  ("KYD",0.8333),
  ("KZT",482.3311),
  ("LAK",16830.6124),
  ("LBP",1507.5000),
  ("LKR",355.9082),
  ("LRD",152.2910),
  ("LSL",16.8374),
  ("LYD",4.8776),
  ("MAD",9.8599),
  ("MDL",19.2852),
  ("MGA",4105.5750),
  ("MKD",60.3193),
  ("MMK",1833.5848),
  ("MNT",3139.6290),
  ("MOP",8.0856),
  ("MRU",37.0591),
  ("MUR",44.4915),
  ("MVR",15.4167),
  ("MWK",1034.1598),
  ("MXN",20.6054),
  ("MYR",4.4468),
  ("MZN",64.6742),
  ("NAD",16.8374),
  ("NGN",414.4834),
  ("NIO",35.7851),
  ("NOK",9.9452),
  ("NPR",127.9413),
  ("NZD",1.6007),
  ("OMR",0.3845),
  ("PAB",1.0000),
  ("PEN",3.9099),
  ("PGK",3.5439),
  ("PHP",56.1811),
  ("PKR",225.5667),
  ("PLN",4.6414),
  ("PYG",6854.1352),
  ("QAR",3.6400),
  ("RON",4.8218),
  ("RSD",114.9675),
  ("RUB",57.8052),
  ("RWF",1047.4216),
  ("SAR",3.7500),
  ("SBD",8.0244),
  ("SCR",12.9799),
  ("SDG",454.9995),
  ("SEK",10.2347),
  ("SGD",1.3858),
  ("SHP",0.8353),
  ("SLE",13.8488),
  ("SLL",13848.8260),
  ("SOS",577.1205),
  ("SRD",22.6182),
  ("SSP",552.6863),
  ("STN",24.0235),
  ("SYP",2467.2810),
  ("SZL",16.8374),
  ("THB",36.7736),
  ("TJS",10.4502),
  ("TMT",3.4991),
  ("TND",2.8636),
  ("TOP",2.3337),
  ("TRY",17.7791),
  ("TTD",6.7760),
  ("TVD",1.4426),
  ("TWD",29.8183),
  ("TZS",2322.0729),
  ("UAH",36.4129),
  ("UGX",3834.6080),
  ("UYU",42.0398),
  ("UZS",10888.2506),
  ("VES",5.7327),
  ("VND",23394.2335),
  ("VUV",117.3470),
  ("WST",2.7009),
  ("XAF",643.2004),
  ("XCD",2.7000),
  ("XDR",0.7625),
  ("XOF",643.2004),
  ("XPF",117.0113),
  ("YER",249.6927),
  ("ZAR",16.8378),
  ("ZMW",16.4868),
  ("ZWL",406.8311)

''')
        conn.commit()


password = input('please enter your database password')
db_instance = DBcon(password)
db_instance.database_generator()
