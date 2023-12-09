import requests
from tqdm import trange

url = 'https://se.ifmo.ru/courses/programming'
headers = {
    'cookie': 'COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=ru_RU; _ga=GA1.2.480364097.1702153636; _gid=GA1.2.1019508200.1702153636; LFR_SESSION_STATE_10158=1702153648858; COMPANY_ID=10154; ID=61386d714357466f78366c65626b42733179393743673d3d; JSESSIONID=vDATCH_zWT6yspi1Tq8KFDu9Ex-tEzKG5gEHPgZv.lportal; LOGIN=73343038313136; PASSWORD=316d3758392b554d565a484137566673746d715574413d3d; REMEMBER_ME=true; SCREEN_NAME=477843484b47726d352f5236684875686242673136413d3d; _gat=1; _ga_5R1ZXK9D1L=GS1.2.1702153635.1.1.1702155035.60.0.0',
}

for i in trange(1, 10000):
    data = requests.post(url, data={'var': i}, headers=headers, params={'p_p_id': 'pbportletlab3_WAR_pbportlet_INSTANCE_JJ2ZU45GpRYN', 'p_p_lifecycle': '1', 'p_p_state': 'normal', 'p_p_mode': 'view', '_pbportletlab3_WAR_pbportlet_INSTANCE_JJ2ZU45GpRYN_javax.portlet.action': 'generate', 'p_auth': 'NiL0qXJD'})
    if 'Увидев, что Незнайка снова закрыл глаза, доктор Пилюлькин принялся трясти его за плечо.' in data.text:
        print(data.text, i)
