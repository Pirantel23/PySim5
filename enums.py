from enum import Enum


class PaymentType(Enum):
    Buy = 'buy'
    Charge = 'charge'


class Status(Enum):
    Pending = 'PENDING'
    Recieved = 'RECEIVED'
    Canceled = 'CANCELED'
    Timeout = 'TIMEOUT'
    Finished = 'FINISHED'
    Banned = 'BANNED'


class Country(Enum):
    Afghanistan = 'afghanistan'
    Albania = 'albania'
    Algeria = 'algeria'
    Angola = 'angola'
    Anguilla = 'anguilla'
    Antiguaandbarbuda = 'antiguaandbarbuda'
    Argentina = 'argentina'
    Armenia = 'armenia'
    Aruba = 'aruba'
    Australia = 'australia'
    Austria = 'austria'
    Azerbaijan = 'azerbaijan'
    Bahamas = 'bahamas'
    Bahrain = 'bahrain'
    Bangladesh = 'bangladesh'
    Barbados = 'barbados'
    Belarus = 'belarus'
    Belgium = 'belgium'
    Belize = 'belize'
    Benin = 'benin'
    Bhutane = 'bhutane'
    Bih = 'bih'
    Bolivia = 'bolivia'
    Botswana = 'botswana'
    Brazil = 'brazil'
    Bulgaria = 'bulgaria'
    Burkinafaso = 'burkinafaso'
    Burundi = 'burundi'
    Cambodia = 'cambodia'
    Cameroon = 'cameroon'
    Canada = 'canada'
    Capeverde = 'capeverde'
    Caymanislands = 'caymanislands'
    Chad = 'chad'
    Chile = 'chile'
    China = 'china'
    Colombia = 'colombia'
    Comoros = 'comoros'
    Congo = 'congo'
    Costarica = 'costarica'
    Croatia = 'croatia'
    Cyprus = 'cyprus'
    Czech = 'czech'
    Djibouti = 'djibouti'
    Dominica = 'dominica'
    Dominicana = 'dominicana'
    Easttimor = 'easttimor'
    Ecuador = 'ecuador'
    Egypt = 'egypt'
    England = 'england'
    Equatorialguinea = 'equatorialguinea'
    Eritrea = 'eritrea'
    Estonia = 'estonia'
    Ethiopia = 'ethiopia'
    Finland = 'finland'
    France = 'france'
    Frenchguiana = 'frenchguiana'
    Gabon = 'gabon'
    Gambia = 'gambia'
    Georgia = 'georgia'
    Germany = 'germany'
    Ghana = 'ghana'
    Greece = 'greece'
    Grenada = 'grenada'
    Guadeloupe = 'guadeloupe'
    Guatemala = 'guatemala'
    Guinea = 'guinea'
    Guineabissau = 'guineabissau'
    Guyana = 'guyana'
    Haiti = 'haiti'
    Honduras = 'honduras'
    Hongkong = 'hongkong'
    Hungary = 'hungary'
    India = 'india'
    Indonesia = 'indonesia'
    Ireland = 'ireland'
    Israel = 'israel'
    Italy = 'italy'
    Ivorycoast = 'ivorycoast'
    Jamaica = 'jamaica'
    Japan = 'japan'
    Jordan = 'jordan'
    Kazakhstan = 'kazakhstan'
    Kenya = 'kenya'
    Kuwait = 'kuwait'
    Kyrgyzstan = 'kyrgyzstan'
    Laos = 'laos'
    Latvia = 'latvia'
    Lesotho = 'lesotho'
    Liberia = 'liberia'
    Lithuania = 'lithuania'
    Luxembourg = 'luxembourg'
    Macau = 'macau'
    Madagascar = 'madagascar'
    Malawi = 'malawi'
    Malaysia = 'malaysia'
    Maldives = 'maldives'
    Mauritania = 'mauritania'
    Mauritius = 'mauritius'
    Mexico = 'mexico'
    Moldova = 'moldova'
    Mongolia = 'mongolia'
    Montenegro = 'montenegro'
    Montserrat = 'montserrat'
    Morocco = 'morocco'
    Mozambique = 'mozambique'
    Myanmar = 'myanmar'
    Namibia = 'namibia'
    Nepal = 'nepal'
    Netherlands = 'netherlands'
    Newcaledonia = 'newcaledonia'
    Newzealand = 'newzealand'
    Nicaragua = 'nicaragua'
    Niger = 'niger'
    Nigeria = 'nigeria'
    Northmacedonia = 'northmacedonia'
    Norway = 'norway'
    Oman = 'oman'
    Pakistan = 'pakistan'
    Panama = 'panama'
    Papuanewguinea = 'papuanewguinea'
    Paraguay = 'paraguay'
    Peru = 'peru'
    Philippines = 'philippines'
    Poland = 'poland'
    Portugal = 'portugal'
    Puertorico = 'puertorico'
    Reunion = 'reunion'
    Romania = 'romania'
    Russia = 'russia'
    Rwanda = 'rwanda'
    Saintkittsandnevis = 'saintkittsandnevis'
    Saintlucia = 'saintlucia'
    Saintvincentandgrenadines = 'saintvincentandgrenadines'
    Salvador = 'salvador'
    Samoa = 'samoa'
    Saotomeandprincipe = 'saotomeandprincipe'
    Saudiarabia = 'saudiarabia'
    Senegal = 'senegal'
    Serbia = 'serbia'
    Seychelles = 'seychelles'
    Sierraleone = 'sierraleone'
    Singapore = 'singapore'
    Slovakia = 'slovakia'
    Slovenia = 'slovenia'
    Solomonislands = 'solomonislands'
    Southafrica = 'southafrica'
    Spain = 'spain'
    Srilanka = 'srilanka'
    Suriname = 'suriname'
    Swaziland = 'swaziland'
    Sweden = 'sweden'
    Switzerland = 'switzerland'
    Taiwan = 'taiwan'
    Tajikistan = 'tajikistan'
    Tanzania = 'tanzania'
    Thailand = 'thailand'
    Tit = 'tit'
    Togo = 'togo'
    Tonga = 'tonga'
    Tunisia = 'tunisia'
    Turkey = 'turkey'
    Turkmenistan = 'turkmenistan'
    Turksandcaicos = 'turksandcaicos'
    Uganda = 'uganda'
    Ukraine = 'ukraine'
    Uruguay = 'uruguay'
    Usa = 'usa'
    Uzbekistan = 'uzbekistan'
    Venezuela = 'venezuela'
    Vietnam = 'vietnam'
    Virginislands = 'virginislands'
    Zambia = 'zambia'
    Zimbabwe = 'zimbabwe'


class Target(Enum):
    Ace2three = 'ace2three'
    Adidas = 'adidas'
    Agroinform = 'agroinform'
    Airbnb = 'airbnb'
    Airtel = 'airtel'
    Aitu = 'aitu'
    Akelni = 'akelni'
    Alfa = 'alfa'
    Algida = 'algida'
    Alibaba = 'alibaba'
    Aliexpress = 'aliexpress'
    Alipay = 'alipay'
    Amasia = 'amasia'
    Amazon = 'amazon'
    Aol = 'aol'
    Apple = 'apple'
    Astropay = 'astropay'
    Auchan = 'auchan'
    Avito = 'avito'
    Avon = 'avon'
    Azino = 'azino'
    B4ucabs = 'b4ucabs'
    Baidu = 'baidu'
    Banqi = 'banqi'
    Bigolive = 'bigolive'
    Billmill = 'billmill'
    Bisu = 'bisu'
    Bitaqaty = 'bitaqaty'
    Bitclout = 'bitclout'
    Bittube = 'bittube'
    Blablacar = 'blablacar'
    Blizzard = 'blizzard'
    Blockchain = 'blockchain'
    Blued = 'blued'
    Bolt = 'bolt'
    Brand20ua = 'brand20ua'
    Burgerking = 'burgerking'
    Bykea = 'bykea'
    Cafebazaar = 'cafebazaar'
    Caixa = 'caixa'
    Careem = 'careem'
    Carousell = 'carousell'
    Cdkeys = 'cdkeys'
    Cekkazan = 'cekkazan'
    Citaprevia = 'citaprevia'
    Citymobil = 'citymobil'
    Clickentregas = 'clickentregas'
    Cliqq = 'cliqq'
    Clubhouse = 'clubhouse'
    Cmtcuzdan = 'cmtcuzdan'
    Coinbase = 'coinbase'
    Coinfield = 'coinfield'
    Craigslist = 'craigslist'
    Cryptocom = 'cryptocom'
    Dbrua = 'dbrua'
    Deliveroo = 'deliveroo'
    Delivery = 'delivery'
    Dent = 'dent'
    Dhani = 'dhani'
    Didi = 'didi'
    Digikala = 'digikala'
    Discord = 'discord'
    Disneyhotstar = 'disneyhotstar'
    Divar = 'divar'
    Dixy = 'dixy'
    Dodopizza = 'dodopizza'
    Domdara = 'domdara'
    Dominospizza = 'dominospizza'
    Dostavista = 'dostavista'
    Douyu = 'douyu'
    Dream11 = 'dream11'
    Drom = 'drom'
    Drugvokrug = 'drugvokrug'
    Dukascopy = 'dukascopy'
    Easypay = 'easypay'
    Ebay = 'ebay'
    Ebikegewinnspiel = 'ebikegewinnspiel'
    Edgeless = 'edgeless'
    Electroneum = 'electroneum'
    Eneba = 'eneba'
    Ezbuy = 'ezbuy'
    Faberlic = 'faberlic'
    Facebook = 'facebook'
    Fiqsy = 'fiqsy'
    Fiverr = 'fiverr'
    Foodpanda = 'foodpanda'
    Foody = 'foody'
    Forwarding = 'forwarding'
    Freecharge = 'freecharge'
    Galaxy = 'galaxy'
    Gamearena = 'gamearena'
    Gameflip = 'gameflip'
    Gamekit = 'gamekit'
    Gamer = 'gamer'
    Gcash = 'gcash'
    Get = 'get'
    Getir = 'getir'
    Gett = 'gett'
    Gg = 'gg'
    Gittigidiyor = 'gittigidiyor'
    Global24 = 'global24'
    Globaltel = 'globaltel'
    Globus = 'globus'
    Glovo = 'glovo'
    Google = 'google'
    Grabtaxi = 'grabtaxi'
    Green = 'green'
    Grindr = 'grindr'
    Hamrahaval = 'hamrahaval'
    Happn = 'happn'
    Haraj = 'haraj'
    Hepsiburadacom = 'hepsiburadacom'
    Hezzl = 'hezzl'
    Hily = 'hily'
    Hopi = 'hopi'
    Hqtrivia = 'hqtrivia'
    Humblebundle = 'humblebundle'
    Humta = 'humta'
    Huya = 'huya'
    Icard = 'icard'
    Icq = 'icq'
    Icrypex = 'icrypex'
    Ifood = 'ifood'
    Immowelt = 'immowelt'
    Imo = 'imo'
    Inboxlv = 'inboxlv'
    Indriver = 'indriver'
    Ininal = 'ininal'
    Instagram = 'instagram'
    Iost = 'iost'
    Iqos = 'iqos'
    Ivi = 'ivi'
    Iyc = 'iyc'
    Jd = 'jd'
    Jkf = 'jkf'
    Justdating = 'justdating'
    Justdial = 'justdial'
    Kakaotalk = 'kakaotalk'
    Karusel = 'karusel'
    Keybase = 'keybase'
    Komandacard = 'komandacard'
    Kotak811 = 'kotak811'
    Kucoinplay = 'kucoinplay'
    Kufarby = 'kufarby'
    Kvartplata = 'kvartplata'
    Kwai = 'kwai'
    Lazada = 'lazada'
    Lbry = 'lbry'
    Lenta = 'lenta'
    Lianxin = 'lianxin'
    Line = 'line'
    Linkedin = 'linkedin'
    Livescore = 'livescore'
    Magnit = 'magnit'
    Magnolia = 'magnolia'
    Mailru = 'mailru'
    Mamba = 'mamba'
    Mcdonalds = 'mcdonalds'
    Meetme = 'meetme'
    Mega = 'mega'
    Mercado = 'mercado'
    Michat = 'michat'
    Microsoft = 'microsoft'
    Miloan = 'miloan'
    Miratorg = 'miratorg'
    Mobile01 = 'mobile01'
    Momo = 'momo'
    Monese = 'monese'
    Monobank = 'monobank'
    Mosru = 'mosru'
    Mrgreen = 'mrgreen'
    Mtscashback = 'mtscashback'
    Myfishka = 'myfishka'
    Myglo = 'myglo'
    Mylove = 'mylove'
    Mymusictaste = 'mymusictaste'
    Mzadqatar = 'mzadqatar'
    Nana = 'nana'
    Naver = 'naver'
    Ncsoft = 'ncsoft'
    Netflix = 'netflix'
    Nhseven = 'nhseven'
    Nifty = 'nifty'
    Nike = 'nike'
    Nimses = 'nimses'
    Nrjmusicawards = 'nrjmusicawards'
    Nttgame = 'nttgame'
    Odnoklassniki = 'odnoklassniki'
    Offerup = 'offerup'
    Offgamers = 'offgamers'
    Okcupid = 'okcupid'
    Okey = 'okey'
    Okta = 'okta'
    Olacabs = 'olacabs'
    Olx = 'olx'
    Onlinerby = 'onlinerby'
    Openpoint = 'openpoint'
    Oraclecloud = 'oraclecloud'
    Oriflame = 'oriflame'
    Other = 'other'
    Ozon = 'ozon'
    Paddypower = 'paddypower'
    Pairs = 'pairs'
    Papara = 'papara'
    Paxful = 'paxful'
    Payberry = 'payberry'
    Paycell = 'paycell'
    Paymaya = 'paymaya'
    Paypal = 'paypal'
    Paysend = 'paysend'
    Paytm = 'paytm'
    Peoplecom = 'peoplecom'
    Perekrestok = 'perekrestok'
    Pgbonus = 'pgbonus'
    Picpay = 'picpay'
    Pof = 'pof'
    Pokec = 'pokec'
    Pokermaster = 'pokermaster'
    Potato = 'potato'
    Powerkredite = 'powerkredite'
    Prajmeriz2020 = 'prajmeriz2020'
    Premiumone = 'premiumone'
    Prom = 'prom'
    Proton = 'proton'
    Protonmail = 'protonmail'
    Protp = 'protp'
    Pubg = 'pubg'
    Pureplatfrom = 'pureplatfrom'
    Pyaterochka = 'pyaterochka'
    Pyromusic = 'pyromusic'
    Q12trivia = 'q12trivia'
    Qiwiwallet = 'qiwiwallet'
    Quipp = 'quipp'
    Rakuten = 'rakuten'
    Rambler = 'rambler'
    Rediffmail = 'rediffmail'
    Reuse = 'reuse'
    Ripkord = 'ripkord'
    Rosakhutor = 'rosakhutor'
    Rsa = 'rsa'
    Rutube = 'rutube'
    Samokat = 'samokat'
    Seosprint = 'seosprint'
    Sheerid = 'sheerid'
    Shopee = 'shopee'
    Signal = 'signal'
    Sikayetvar = 'sikayetvar'
    Skout = 'skout'
    Snapchat = 'snapchat'
    Snappfood = 'snappfood'
    Sneakersnstuff = 'sneakersnstuff'
    Socios = 'socios'
    Sportmaster = 'sportmaster'
    Spothit = 'spothit'
    Ssoidnet = 'ssoidnet'
    Steam = 'steam'
    Surveytime = 'surveytime'
    Swvl = 'swvl'
    Taksheel = 'taksheel'
    Tango = 'tango'
    Tantan = 'tantan'
    Taobao = 'taobao'
    Telegram = 'telegram'
    Tencentqq = 'tencentqq'
    Ticketmaster = 'ticketmaster'
    Tiktok = 'tiktok'
    Tinder = 'tinder'
    Tosla = 'tosla'
    Totalcoin = 'totalcoin'
    Touchance = 'touchance'
    Trendyol = 'trendyol'
    Truecaller = 'truecaller'
    Twitch = 'twitch'
    Twitter = 'twitter'
    Uber = 'uber'
    Ukrnet = 'ukrnet'
    Uploaded = 'uploaded'
    Vernyi = 'vernyi'
    Vernyj = 'vernyj'
    Viber = 'viber'
    Vitajekspress = 'vitajekspress'
    Vkontakte = 'vkontakte'
    Voopee = 'voopee'
    Wechat = 'wechat'
    Weibo = 'weibo'
    Weku = 'weku'
    Weststein = 'weststein'
    Whatsapp = 'whatsapp'
    Wildberries = 'wildberries'
    Wingmoney = 'wingmoney'
    Winston = 'winston'
    Wish = 'wish'
    Wmaraci = 'wmaraci'
    Wolt = 'wolt'
    Yaay = 'yaay'
    Yahoo = 'yahoo'
    Yalla = 'yalla'
    Yandex = 'yandex'
    Yemeksepeti = 'yemeksepeti'
    Youdo = 'youdo'
    Youla = 'youla'
    Youstar = 'youstar'
    Zalo = 'zalo'
    Zoho = 'zoho'
    Zomato = 'zomato'