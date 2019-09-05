import json
import re
from lxml import etree

from django.shortcuts import render

# Create your views here.
from django.views import View

import requests

from product.models import Original_Products_data
from user.models import User


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class JDview(View):
    def get(self, request):
        return render(request, 'jd.html')

    def post(self, request):
        jd_url = request.POST.get('jd_url')
        context = self.parse_url(jd_url)

        '''
        user_id = models.ForeignKey(User, on_delete=models.CASCADE())
        product_title = models.CharField(max_length=120)
        product_description = models.CharField(max_length=1000)
        product_sku_data = models.CharField(max_length=1000)
        is_th = models.IntegerField(null=True, blank=True)
        is_tw = models.IntegerField(null=True, blank=True)
        is_vn = models.IntegerField(null=True, blank=True)
        is_my = models.IntegerField(null=True, blank=True)
        is_ph = models.IntegerField(null=True, blank=True)
        is_id = models.IntegerField(null=True, blank=True)
        is_sg = models.IntegerField(null=True, blank=True)
        data_source = models.CharField(max_length=1000)
        delete_at = models.DateTimeField(null=True, blank=True)
        '''

        context.update({'product_url': jd_url})
        user = User.objects.all().first()
        print(context['product_desc'])
        product_desc = re.findall('>(.*?)<', context['product_desc'], re.S)
        if product_desc == '':
            product_desc = context['product_desc']
        print(product_desc)
        Original_Products_data.objects.create(
            user_id=user,
            product_title=context['product_name'],
            product_description=product_desc,
            product_sku_data=context['product_style'],
            data_source=context['product_url']
        )

        return render(request, 'jd_detail.html', context)

    def parse_url(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
        }
        html = requests.get(url=url, headers=headers).content.decode()
        tree = etree.HTML(html)
        product_name = tree.xpath('//div[@class="p-head-text"]/h1/@title')[0]
        print(product_name)
        product_price = re.findall(',"value":"(.*?)"}', html, re.S)[0]
        print(product_price)
        product_id = re.findall('"wareId":"(.*?)","', html, re.S)[0]

        product_style = re.findall('"colorSize":.*?{"text":"(.*?)","no', html, re.S)[0]

        product_size = re.findall('{"text":"(.*?)","no', html, re.S)

        product_img = re.findall('"image":"(.*?)",', html, re.S)

        product_other_imgs = re.findall('{"big":"(.*?)","', html, re.S)

        detail_url = 'https://api.jd.co.th/client.action?lang=th_TH&client=pc&functionId=wareIntroView&body={"wareId":"%s","displayTxtOrHtml":"html"}' % product_id

        html_info = requests.get(url=detail_url, headers=headers).content.decode()

        info = json.loads(html_info)
        product_desc = info['wareIntro']
        context = {
            'product_id': product_id,
            'product_name': product_name,
            'product_price': product_price,
            'product_style': product_style,
            'product_size': product_size,
            'product_img': product_img,
            'product_other_imgs': product_other_imgs,
            'product_desc': product_desc,
        }
        return context


def insert_db(data):
    pass
