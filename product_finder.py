import requests
from product import Product


class ProductFinder:
    def __init__(self):
        self.term = ''
        self.suggestions = []
        self.products = {}

    def get_suggestions(self):
        cookies = {
            'localStoreInfo': 'eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9',
            'deliveryCatchment': '1061',
            'walmart.shippingPostalCode': 'L5V2N6',
            'defaultNearestStoreId': '1061',
            'wmt.c': '0',
            'vtc': 'S0V516wJjI2AAOb67ETj7g',
            'userSegment': '10-percent',
            'walmart.nearestLatLng': '"43.8483,-79.3349"',
            'walmart.id': '7e63d549-4f12-4e60-89a3-336858345955',
            '_gcl_au': '1.1.2070437989.1661033248',
            'DYN_USER_ID': '8ccca502-bb83-49c3-8a59-0065615a134d',
            'WM_SEC.AUTH_TOKEN': 'MTAyOTYyMDE4892TaUaERPaFJ1ZzqPQe2YtUSZTwxe8fs5K1tFPfr2rLqxfUizCyFgYibrn6+OkI9ugJVTg2wpbZtSHpeKvM4qxoO7XjG6us90cMLdpkYNcj80JF07g1vbZLKpwu7N3gj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj3q+sxGPiNWrB2amHKKiX2S42068UyLzo6DZUe4HG93fpQ2Tb7w+T0sRXSVmjJQd9Lb/SoGFgAYL9DGZ8K45WCXM/FHGZ2dCNmxWrdkwqEKrt821pAn2E5aDsnhYCCZKDAZUfaJV09dWZAaPPoL0DTkO2cN6PFGnxcmaMTzQIvEBfq2RBtC3e+zyJ8k1hTJn1bCqDbHqzyLX19PYm8H+OfNpKyn8GJqhjhOBicQkFdiGkr1eX9YGQ0laieVMoEr348=',
            'LT': '1661033249135',
            'DYN_USER_ID.ro': '8ccca502-bb83-49c3-8a59-0065615a134d',
            'pxcts': '7b57f990-20d4-11ed-b745-516c466f5543',
            '_pxvid': '7b57ee8c-20d4-11ed-b745-516c466f5543',
            '_ga': 'GA1.2.1891062393.1661033249',
            '_gid': 'GA1.2.958446820.1661033249',
            '_cs_c': '1',
            's_ecid': 'MCMID%7C34697214536144180794224801759592372312',
            'AMCVS_C4C6370453309C960A490D44%40AdobeOrg': '1',
            '__gads': 'ID=85778bf916199b20-2260cf72b9d40031:T=1661033249:S=ALNI_MbtlT-8qJfXAkD3Bg1yMwpCifvoZQ',
            '__gpi': 'UID=000008021c6d9707:T=1661033249:RT=1661033249:S=ALNI_MZjCN2tQ24WzDAw_MGJpBuvNlxZrw',
            's_cc': 'true',
            '_fbp': 'fb.1.1661033249952.1937814821',
            'kndctr_C4C6370453309C960A490D44_AdobeOrg_identity': 'CiYzNDY5NzIxNDUzNjE0NDE4MDc5NDIyNDgwMTc1OTU5MjM3MjMxMlIOCKT8r-qrMBgBKgNWQTbwAaT8r-qrMA==',
            '_4c_': '%7B%22_4c_mc_%22%3A%22dd5400b5-3ee4-4cd2-9069-dabc7628b8a5%22%7D',
            'NEXT_GEN.ENABLED': '1',
            'cartId': 'b6a2ce77-0880-4950-b035-bde64042746a',
            '_scid': '16b0d277-69c4-4649-9eb7-aacf33fb0eb0',
            '_pin_unauth': 'dWlkPVlqRXlabVE0WmpRdFptWTJPUzAwTXpJMkxXRTJNRE10WlRZNE1tUTRNR00wTldabA',
            'BVBRANDID': 'dc782732-2ebe-4fc3-bacf-f3553c2ba90d',
            'BVImplmain_site': '2036',
            'ENV': 'ak-eus-t1-prod',
            'bstc': 'cOgytbuHSUBJ3XXBCcQIBs',
            'xpa': '--jYu|-99OH|1sIDy|2lwWQ|3zyae|59Tck|5p0A0|5p25F|7QNwp|7Xi3l|8C3ux|9ZcI6|9jPmV|AuvWK|D4f_q|D9LOQ|EF9Bs|EL3ho|ENqC6|F6obB|FtRSv|H33MR|H67lQ|HKhPY|HRTLp|HTPms|HW-Xl|Hoe5J|I9Jw3|II82a|IVqRT|J6lpV|JOdOP|JoXRc|JvV8u|KERNb|KeAz7|MbHLZ|NOaJP|NPyyt|NbKZN|OVStb|OgGb6|PEwcJ|PHaOk|PMYXx|R79oz|RG5Bo|Ru7oD|S0hIk|Sow5W|Sq5sb|T0TXC|T4DD-|V3_qS|VBVd7|W-D6M|XDZ51|XpoJ0|YmdKw|_IueI|_J9It|_lDzX|_vHmT|_vY-K|a4fYU|aVJBH|amlzz|dQFBj|eDgDq|ep_RO|htzpo|jeBOs|kCz1y|m2qz0|mOlOu|mfKI8|njl-a|p1Ejf|rWfNO|sbXJ0|tnV6l|uBlcT|u_M4R|v-FRz|vm9yl|wI_Ba|wKkZZ|xafoR|yAFBx',
            'exp-ck': '--jYu11sIDy13zyae159Tck15p25F17QNwp17Xi3l18C3ux39ZcI619jPmV1AuvWK1D4f_q1D9LOQ2EF9Bs1EL3ho1F6obB1FtRSv1H33MR1H67lQ6HKhPY1HTPms1HW-Xl8Hoe5J1I9Jw31II82a7IVqRT1JOdOP1JoXRc1JvV8u1KERNb3KeAz71MbHLZ1NPyyt4NbKZN5OVStb1OgGb61R79oz1RG5Bo4Ru7oD1S0hIk1Sow5W1Sq5sb1T4DD-5V3_qS1XDZ511XpoJ01YmdKw1_IueI1_J9It1_vHmT1amlzz1eDgDq1ep_RO1htzpo1kCz1y1m2qz01mfKI81p1Ejf1rWfNO4sbXJ01tnV6l3uBlcT1u_M4R2v-FRz6vm9yl1wI_Ba1wKkZZ1yAFBx1',
            'ak_bmsc': '46A487EE9C06D338F0012EDFE1ADF012~000000000000000000000000000000~YAAQ2a9FQwHIhbGCAQAACVHXvRBxdjUQu86R5S3ujXHXOMr3h6Yz1t8nGx41yx+SOWdRL17ibXiwbJ5nsG8KWJTnXdS6tKfk1G9PpsTkhMHa1uS4nA5jUyRV1NV7QicNd90UIvjUVyov3Nhmn+X00xrYgRUb2z4miE3q66Xc8AF4XjCiMrj8YkUUQkAnUWsp15YJQ3YI7fX9b5/gch9PZP9nqeXwK23v4DG120qTWg0Nla32glNbjxKENqauvFcRO8RwX+0JRQxI/8WTox4qNqMV06wZc3NIU8oWJMhDhqb/jv9VFPZz1Z6bQewlqS9Aj7rKAP2reJb3gI3jqY88Z16u2O0bjSGcSxL6KhPzyWfRYiPih0uGnaenJAwgl/S5O2omXtTbRJo=',
            'xpm': '1%2B1661042380%2BS0V516wJjI2AAOb67ETj7g~%2B0',
            's_visit': '1',
            'AMCV_C4C6370453309C960A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C19225%7CMCMID%7C34697214536144180794224801759592372312%7CMCAID%7CNONE%7CMCOPTOUT-1661049670s%7CNONE%7CMCAAMLH-1661647270%7C7%7CMCAAMB-1661647270%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19232%7CvVersion%7C5.2.0',
            'kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster': 'va6',
            'headerType': 'grocery',
            '_uetsid': '782d818020d511ed9b12b31ed0dde046',
            '_uetvid': '782e629020d511edbde39f4ef7a55986',
            '_cs_cvars': '%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D',
            'walmart.nearestPostalCode': 'L3R9Z0',
            's_gnr': '1661043673308-Repeat',
            'gpv_Page': 'Search%3A%20broc%3A%20Grocery',
            'cto_bundle': '0hxtX185RnR6RlIwejJjV2R0Nm10SThCNURlYyUyQiUyRkVJV1JadGI0UFF3VUNsRkJ4TWxMUUQ2VzBIb3V4VVJQdHdGYjdtTTQ5bUNKWGd3aHVLSW5VS01Xb1lxdUd2RE1vcG1aUW02TWRHdko3cVN4RkklMkZsN1hMS0pNOXpJOWJIcVZUMlRyRw',
            'authDuration': '{"lat":"1661043673951000","lt":"1661043673951000"}',
            '_cs_id': 'e2503a21-8c83-a3f0-9f3f-e297ecbf2988.1661033248.3.1661043673.1661042337.1.1695197248874',
            '_cs_s': '6.0.0.1661045473523',
            'TS0196c61b': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            'TS017d5bf6': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            'TS01170c9f': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            'seqnum': '64',
            'bm_sv': '97C9C791EC3108D91A1969E95338BEA1~YAAQJQ/QFyBuVLWCAQAAIOzrvRBTn+ARHcT0+QwA41WNAnemChf3jxvvgLnzfeR3O5b4LCcfxXh/a1CFeKV9qHr0D47F1JISnKu1bb5iYNTPQsNa/b6qGmgjBHpRtfS76yoM1w4uzIQwQdSqhXZ+2NdExbEVozZNfwCow3McXt/mTDePLYudsKr0VpH7+KENxpvuhJCZzKJPCoz2iMF+GOZNIerXlGMlwPVbZ9sAKE8Kgi/yB1Nj+K6F80DDJQWUuA==~1',
            's_sq': '%5B%5BB%5D%5D',
        }

        headers = {
            'authority': 'www.walmart.ca',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; wmt.c=0; vtc=S0V516wJjI2AAOb67ETj7g; userSegment=10-percent; walmart.nearestLatLng="43.8483,-79.3349"; walmart.id=7e63d549-4f12-4e60-89a3-336858345955; _gcl_au=1.1.2070437989.1661033248; DYN_USER_ID=8ccca502-bb83-49c3-8a59-0065615a134d; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4892TaUaERPaFJ1ZzqPQe2YtUSZTwxe8fs5K1tFPfr2rLqxfUizCyFgYibrn6+OkI9ugJVTg2wpbZtSHpeKvM4qxoO7XjG6us90cMLdpkYNcj80JF07g1vbZLKpwu7N3gj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj3q+sxGPiNWrB2amHKKiX2S42068UyLzo6DZUe4HG93fpQ2Tb7w+T0sRXSVmjJQd9Lb/SoGFgAYL9DGZ8K45WCXM/FHGZ2dCNmxWrdkwqEKrt821pAn2E5aDsnhYCCZKDAZUfaJV09dWZAaPPoL0DTkO2cN6PFGnxcmaMTzQIvEBfq2RBtC3e+zyJ8k1hTJn1bCqDbHqzyLX19PYm8H+OfNpKyn8GJqhjhOBicQkFdiGkr1eX9YGQ0laieVMoEr348=; LT=1661033249135; DYN_USER_ID.ro=8ccca502-bb83-49c3-8a59-0065615a134d; pxcts=7b57f990-20d4-11ed-b745-516c466f5543; _pxvid=7b57ee8c-20d4-11ed-b745-516c466f5543; _ga=GA1.2.1891062393.1661033249; _gid=GA1.2.958446820.1661033249; _cs_c=1; s_ecid=MCMID%7C34697214536144180794224801759592372312; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; __gads=ID=85778bf916199b20-2260cf72b9d40031:T=1661033249:S=ALNI_MbtlT-8qJfXAkD3Bg1yMwpCifvoZQ; __gpi=UID=000008021c6d9707:T=1661033249:RT=1661033249:S=ALNI_MZjCN2tQ24WzDAw_MGJpBuvNlxZrw; s_cc=true; _fbp=fb.1.1661033249952.1937814821; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYzNDY5NzIxNDUzNjE0NDE4MDc5NDIyNDgwMTc1OTU5MjM3MjMxMlIOCKT8r-qrMBgBKgNWQTbwAaT8r-qrMA==; _4c_=%7B%22_4c_mc_%22%3A%22dd5400b5-3ee4-4cd2-9069-dabc7628b8a5%22%7D; NEXT_GEN.ENABLED=1; cartId=b6a2ce77-0880-4950-b035-bde64042746a; _scid=16b0d277-69c4-4649-9eb7-aacf33fb0eb0; _pin_unauth=dWlkPVlqRXlabVE0WmpRdFptWTJPUzAwTXpJMkxXRTJNRE10WlRZNE1tUTRNR00wTldabA; BVBRANDID=dc782732-2ebe-4fc3-bacf-f3553c2ba90d; BVImplmain_site=2036; ENV=ak-eus-t1-prod; bstc=cOgytbuHSUBJ3XXBCcQIBs; xpa=--jYu|-99OH|1sIDy|2lwWQ|3zyae|59Tck|5p0A0|5p25F|7QNwp|7Xi3l|8C3ux|9ZcI6|9jPmV|AuvWK|D4f_q|D9LOQ|EF9Bs|EL3ho|ENqC6|F6obB|FtRSv|H33MR|H67lQ|HKhPY|HRTLp|HTPms|HW-Xl|Hoe5J|I9Jw3|II82a|IVqRT|J6lpV|JOdOP|JoXRc|JvV8u|KERNb|KeAz7|MbHLZ|NOaJP|NPyyt|NbKZN|OVStb|OgGb6|PEwcJ|PHaOk|PMYXx|R79oz|RG5Bo|Ru7oD|S0hIk|Sow5W|Sq5sb|T0TXC|T4DD-|V3_qS|VBVd7|W-D6M|XDZ51|XpoJ0|YmdKw|_IueI|_J9It|_lDzX|_vHmT|_vY-K|a4fYU|aVJBH|amlzz|dQFBj|eDgDq|ep_RO|htzpo|jeBOs|kCz1y|m2qz0|mOlOu|mfKI8|njl-a|p1Ejf|rWfNO|sbXJ0|tnV6l|uBlcT|u_M4R|v-FRz|vm9yl|wI_Ba|wKkZZ|xafoR|yAFBx; exp-ck=--jYu11sIDy13zyae159Tck15p25F17QNwp17Xi3l18C3ux39ZcI619jPmV1AuvWK1D4f_q1D9LOQ2EF9Bs1EL3ho1F6obB1FtRSv1H33MR1H67lQ6HKhPY1HTPms1HW-Xl8Hoe5J1I9Jw31II82a7IVqRT1JOdOP1JoXRc1JvV8u1KERNb3KeAz71MbHLZ1NPyyt4NbKZN5OVStb1OgGb61R79oz1RG5Bo4Ru7oD1S0hIk1Sow5W1Sq5sb1T4DD-5V3_qS1XDZ511XpoJ01YmdKw1_IueI1_J9It1_vHmT1amlzz1eDgDq1ep_RO1htzpo1kCz1y1m2qz01mfKI81p1Ejf1rWfNO4sbXJ01tnV6l3uBlcT1u_M4R2v-FRz6vm9yl1wI_Ba1wKkZZ1yAFBx1; ak_bmsc=46A487EE9C06D338F0012EDFE1ADF012~000000000000000000000000000000~YAAQ2a9FQwHIhbGCAQAACVHXvRBxdjUQu86R5S3ujXHXOMr3h6Yz1t8nGx41yx+SOWdRL17ibXiwbJ5nsG8KWJTnXdS6tKfk1G9PpsTkhMHa1uS4nA5jUyRV1NV7QicNd90UIvjUVyov3Nhmn+X00xrYgRUb2z4miE3q66Xc8AF4XjCiMrj8YkUUQkAnUWsp15YJQ3YI7fX9b5/gch9PZP9nqeXwK23v4DG120qTWg0Nla32glNbjxKENqauvFcRO8RwX+0JRQxI/8WTox4qNqMV06wZc3NIU8oWJMhDhqb/jv9VFPZz1Z6bQewlqS9Aj7rKAP2reJb3gI3jqY88Z16u2O0bjSGcSxL6KhPzyWfRYiPih0uGnaenJAwgl/S5O2omXtTbRJo=; xpm=1%2B1661042380%2BS0V516wJjI2AAOb67ETj7g~%2B0; s_visit=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19225%7CMCMID%7C34697214536144180794224801759592372312%7CMCAID%7CNONE%7CMCOPTOUT-1661049670s%7CNONE%7CMCAAMLH-1661647270%7C7%7CMCAAMB-1661647270%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19232%7CvVersion%7C5.2.0; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=va6; headerType=grocery; _uetsid=782d818020d511ed9b12b31ed0dde046; _uetvid=782e629020d511edbde39f4ef7a55986; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D; walmart.nearestPostalCode=L3R9Z0; s_gnr=1661043673308-Repeat; gpv_Page=Search%3A%20broc%3A%20Grocery; cto_bundle=0hxtX185RnR6RlIwejJjV2R0Nm10SThCNURlYyUyQiUyRkVJV1JadGI0UFF3VUNsRkJ4TWxMUUQ2VzBIb3V4VVJQdHdGYjdtTTQ5bUNKWGd3aHVLSW5VS01Xb1lxdUd2RE1vcG1aUW02TWRHdko3cVN4RkklMkZsN1hMS0pNOXpJOWJIcVZUMlRyRw; authDuration={"lat":"1661043673951000","lt":"1661043673951000"}; _cs_id=e2503a21-8c83-a3f0-9f3f-e297ecbf2988.1661033248.3.1661043673.1661042337.1.1695197248874; _cs_s=6.0.0.1661045473523; TS0196c61b=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; TS017d5bf6=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; TS01170c9f=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; seqnum=64; bm_sv=97C9C791EC3108D91A1969E95338BEA1~YAAQJQ/QFyBuVLWCAQAAIOzrvRBTn+ARHcT0+QwA41WNAnemChf3jxvvgLnzfeR3O5b4LCcfxXh/a1CFeKV9qHr0D47F1JISnKu1bb5iYNTPQsNa/b6qGmgjBHpRtfS76yoM1w4uzIQwQdSqhXZ+2NdExbEVozZNfwCow3McXt/mTDePLYudsKr0VpH7+KENxpvuhJCZzKJPCoz2iMF+GOZNIerXlGMlwPVbZ9sAKE8Kgi/yB1Nj+K6F80DDJQWUuA==~1; s_sq=%5B%5BB%5D%5D',
            'referer': 'https://www.walmart.ca/search?q=broc&c=10019',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'wm_qos.correlation_id': '87f9ae7b-028-182bdeb06be7e9,87f9ae7b-028-182bdeb06be7ac,87f9ae7b-028-182bdeb06be7ac',
        }

        params = {
            'category': '10019',
            'useTangoId': 'true',
            'prefix': self.term,
            'lang': 'en',
        }

        response = requests.get(
            'https://www.walmart.ca/api/bsp/typeahead/terms', params=params,
            cookies=cookies, headers=headers).json()

        self.suggestions = [response[i]['suggestion'] for i in range(len(response))]

    def get_products(self):
        cookies = {
            'localStoreInfo': 'eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9',
            'deliveryCatchment': '1061',
            'walmart.shippingPostalCode': 'L5V2N6',
            'defaultNearestStoreId': '1061',
            'wmt.c': '0',
            'vtc': 'S0V516wJjI2AAOb67ETj7g',
            'userSegment': '10-percent',
            'walmart.nearestLatLng': '"43.8483,-79.3349"',
            'walmart.id': '7e63d549-4f12-4e60-89a3-336858345955',
            '_gcl_au': '1.1.2070437989.1661033248',
            'DYN_USER_ID': '8ccca502-bb83-49c3-8a59-0065615a134d',
            'WM_SEC.AUTH_TOKEN': 'MTAyOTYyMDE4892TaUaERPaFJ1ZzqPQe2YtUSZTwxe8fs5K1tFPfr2rLqxfUizCyFgYibrn6+OkI9ugJVTg2wpbZtSHpeKvM4qxoO7XjG6us90cMLdpkYNcj80JF07g1vbZLKpwu7N3gj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj3q+sxGPiNWrB2amHKKiX2S42068UyLzo6DZUe4HG93fpQ2Tb7w+T0sRXSVmjJQd9Lb/SoGFgAYL9DGZ8K45WCXM/FHGZ2dCNmxWrdkwqEKrt821pAn2E5aDsnhYCCZKDAZUfaJV09dWZAaPPoL0DTkO2cN6PFGnxcmaMTzQIvEBfq2RBtC3e+zyJ8k1hTJn1bCqDbHqzyLX19PYm8H+OfNpKyn8GJqhjhOBicQkFdiGkr1eX9YGQ0laieVMoEr348=',
            'LT': '1661033249135',
            'DYN_USER_ID.ro': '8ccca502-bb83-49c3-8a59-0065615a134d',
            'pxcts': '7b57f990-20d4-11ed-b745-516c466f5543',
            '_pxvid': '7b57ee8c-20d4-11ed-b745-516c466f5543',
            '_ga': 'GA1.2.1891062393.1661033249',
            '_gid': 'GA1.2.958446820.1661033249',
            '_cs_c': '1',
            's_ecid': 'MCMID%7C34697214536144180794224801759592372312',
            'AMCVS_C4C6370453309C960A490D44%40AdobeOrg': '1',
            '__gads': 'ID=85778bf916199b20-2260cf72b9d40031:T=1661033249:S=ALNI_MbtlT-8qJfXAkD3Bg1yMwpCifvoZQ',
            '__gpi': 'UID=000008021c6d9707:T=1661033249:RT=1661033249:S=ALNI_MZjCN2tQ24WzDAw_MGJpBuvNlxZrw',
            's_cc': 'true',
            '_fbp': 'fb.1.1661033249952.1937814821',
            'kndctr_C4C6370453309C960A490D44_AdobeOrg_identity': 'CiYzNDY5NzIxNDUzNjE0NDE4MDc5NDIyNDgwMTc1OTU5MjM3MjMxMlIOCKT8r-qrMBgBKgNWQTbwAaT8r-qrMA==',
            '_4c_': '%7B%22_4c_mc_%22%3A%22dd5400b5-3ee4-4cd2-9069-dabc7628b8a5%22%7D',
            'NEXT_GEN.ENABLED': '1',
            'cartId': 'b6a2ce77-0880-4950-b035-bde64042746a',
            '_scid': '16b0d277-69c4-4649-9eb7-aacf33fb0eb0',
            '_pin_unauth': 'dWlkPVlqRXlabVE0WmpRdFptWTJPUzAwTXpJMkxXRTJNRE10WlRZNE1tUTRNR00wTldabA',
            'BVBRANDID': 'dc782732-2ebe-4fc3-bacf-f3553c2ba90d',
            'BVImplmain_site': '2036',
            'ENV': 'ak-eus-t1-prod',
            'bstc': 'cOgytbuHSUBJ3XXBCcQIBs',
            'xpa': '--jYu|-99OH|1sIDy|2lwWQ|3zyae|59Tck|5p0A0|5p25F|7QNwp|7Xi3l|8C3ux|9ZcI6|9jPmV|AuvWK|D4f_q|D9LOQ|EF9Bs|EL3ho|ENqC6|F6obB|FtRSv|H33MR|H67lQ|HKhPY|HRTLp|HTPms|HW-Xl|Hoe5J|I9Jw3|II82a|IVqRT|J6lpV|JOdOP|JoXRc|JvV8u|KERNb|KeAz7|MbHLZ|NOaJP|NPyyt|NbKZN|OVStb|OgGb6|PEwcJ|PHaOk|PMYXx|R79oz|RG5Bo|Ru7oD|S0hIk|Sow5W|Sq5sb|T0TXC|T4DD-|V3_qS|VBVd7|W-D6M|XDZ51|XpoJ0|YmdKw|_IueI|_J9It|_lDzX|_vHmT|_vY-K|a4fYU|aVJBH|amlzz|dQFBj|eDgDq|ep_RO|htzpo|jeBOs|kCz1y|m2qz0|mOlOu|mfKI8|njl-a|p1Ejf|rWfNO|sbXJ0|tnV6l|uBlcT|u_M4R|v-FRz|vm9yl|wI_Ba|wKkZZ|xafoR|yAFBx',
            'exp-ck': '--jYu11sIDy13zyae159Tck15p25F17QNwp17Xi3l18C3ux39ZcI619jPmV1AuvWK1D4f_q1D9LOQ2EF9Bs1EL3ho1F6obB1FtRSv1H33MR1H67lQ6HKhPY1HTPms1HW-Xl8Hoe5J1I9Jw31II82a7IVqRT1JOdOP1JoXRc1JvV8u1KERNb3KeAz71MbHLZ1NPyyt4NbKZN5OVStb1OgGb61R79oz1RG5Bo4Ru7oD1S0hIk1Sow5W1Sq5sb1T4DD-5V3_qS1XDZ511XpoJ01YmdKw1_IueI1_J9It1_vHmT1amlzz1eDgDq1ep_RO1htzpo1kCz1y1m2qz01mfKI81p1Ejf1rWfNO4sbXJ01tnV6l3uBlcT1u_M4R2v-FRz6vm9yl1wI_Ba1wKkZZ1yAFBx1',
            'ak_bmsc': '46A487EE9C06D338F0012EDFE1ADF012~000000000000000000000000000000~YAAQ2a9FQwHIhbGCAQAACVHXvRBxdjUQu86R5S3ujXHXOMr3h6Yz1t8nGx41yx+SOWdRL17ibXiwbJ5nsG8KWJTnXdS6tKfk1G9PpsTkhMHa1uS4nA5jUyRV1NV7QicNd90UIvjUVyov3Nhmn+X00xrYgRUb2z4miE3q66Xc8AF4XjCiMrj8YkUUQkAnUWsp15YJQ3YI7fX9b5/gch9PZP9nqeXwK23v4DG120qTWg0Nla32glNbjxKENqauvFcRO8RwX+0JRQxI/8WTox4qNqMV06wZc3NIU8oWJMhDhqb/jv9VFPZz1Z6bQewlqS9Aj7rKAP2reJb3gI3jqY88Z16u2O0bjSGcSxL6KhPzyWfRYiPih0uGnaenJAwgl/S5O2omXtTbRJo=',
            'xpm': '1%2B1661042380%2BS0V516wJjI2AAOb67ETj7g~%2B0',
            's_visit': '1',
            'AMCV_C4C6370453309C960A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C19225%7CMCMID%7C34697214536144180794224801759592372312%7CMCAID%7CNONE%7CMCOPTOUT-1661049670s%7CNONE%7CMCAAMLH-1661647270%7C7%7CMCAAMB-1661647270%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19232%7CvVersion%7C5.2.0',
            'kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster': 'va6',
            'headerType': 'grocery',
            '_uetsid': '782d818020d511ed9b12b31ed0dde046',
            '_uetvid': '782e629020d511edbde39f4ef7a55986',
            '_cs_cvars': '%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D',
            'walmart.nearestPostalCode': 'L3R9Z0',
            's_gnr': '1661043673308-Repeat',
            'gpv_Page': 'Search%3A%20broc%3A%20Grocery',
            'cto_bundle': '0hxtX185RnR6RlIwejJjV2R0Nm10SThCNURlYyUyQiUyRkVJV1JadGI0UFF3VUNsRkJ4TWxMUUQ2VzBIb3V4VVJQdHdGYjdtTTQ5bUNKWGd3aHVLSW5VS01Xb1lxdUd2RE1vcG1aUW02TWRHdko3cVN4RkklMkZsN1hMS0pNOXpJOWJIcVZUMlRyRw',
            'authDuration': '{"lat":"1661043673951000","lt":"1661043673951000"}',
            '_cs_id': 'e2503a21-8c83-a3f0-9f3f-e297ecbf2988.1661033248.3.1661043673.1661042337.1.1695197248874',
            '_cs_s': '6.0.0.1661045473523',
            'TS017d5bf6': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            'TS01170c9f': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            's_sq': '%5B%5BB%5D%5D',
            'seqnum': '65',
            'TS0196c61b': '01538efd7cdef6bfdfd2863a269423f69963070a40b08b3881ee9ba9bcc9834554f37fdf989f452842959f722a64319526c54ede4d',
            'bm_sv': '97C9C791EC3108D91A1969E95338BEA1~YAAQFQ/QF4s5l7mCAQAABHf6vRBAwFCuEqoicWEXpYo0cb5wtzEGU38OechKpKx4r1NJqOYGYMjdTQ/617NzbXNeVc24WV0ArJtObbngdRPtV6hX60/91IMYTRBWdWjF7BRib3q3xkpZWreuHr70KAI/MtNtOmWWKFXZATfY+bJLGAooZE6fL3ruZ1JkmYJtnK+eH2q7/s9yiNKvDpQCdUhARhflhcc2Hhvg5IEYtPEhRCBc0zSGn84r91Dbe4RRnw==~1',
        }

        headers = {
            'authority': 'www.walmart.ca',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; wmt.c=0; vtc=S0V516wJjI2AAOb67ETj7g; userSegment=10-percent; walmart.nearestLatLng="43.8483,-79.3349"; walmart.id=7e63d549-4f12-4e60-89a3-336858345955; _gcl_au=1.1.2070437989.1661033248; DYN_USER_ID=8ccca502-bb83-49c3-8a59-0065615a134d; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4892TaUaERPaFJ1ZzqPQe2YtUSZTwxe8fs5K1tFPfr2rLqxfUizCyFgYibrn6+OkI9ugJVTg2wpbZtSHpeKvM4qxoO7XjG6us90cMLdpkYNcj80JF07g1vbZLKpwu7N3gj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj3q+sxGPiNWrB2amHKKiX2S42068UyLzo6DZUe4HG93fpQ2Tb7w+T0sRXSVmjJQd9Lb/SoGFgAYL9DGZ8K45WCXM/FHGZ2dCNmxWrdkwqEKrt821pAn2E5aDsnhYCCZKDAZUfaJV09dWZAaPPoL0DTkO2cN6PFGnxcmaMTzQIvEBfq2RBtC3e+zyJ8k1hTJn1bCqDbHqzyLX19PYm8H+OfNpKyn8GJqhjhOBicQkFdiGkr1eX9YGQ0laieVMoEr348=; LT=1661033249135; DYN_USER_ID.ro=8ccca502-bb83-49c3-8a59-0065615a134d; pxcts=7b57f990-20d4-11ed-b745-516c466f5543; _pxvid=7b57ee8c-20d4-11ed-b745-516c466f5543; _ga=GA1.2.1891062393.1661033249; _gid=GA1.2.958446820.1661033249; _cs_c=1; s_ecid=MCMID%7C34697214536144180794224801759592372312; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; __gads=ID=85778bf916199b20-2260cf72b9d40031:T=1661033249:S=ALNI_MbtlT-8qJfXAkD3Bg1yMwpCifvoZQ; __gpi=UID=000008021c6d9707:T=1661033249:RT=1661033249:S=ALNI_MZjCN2tQ24WzDAw_MGJpBuvNlxZrw; s_cc=true; _fbp=fb.1.1661033249952.1937814821; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYzNDY5NzIxNDUzNjE0NDE4MDc5NDIyNDgwMTc1OTU5MjM3MjMxMlIOCKT8r-qrMBgBKgNWQTbwAaT8r-qrMA==; _4c_=%7B%22_4c_mc_%22%3A%22dd5400b5-3ee4-4cd2-9069-dabc7628b8a5%22%7D; NEXT_GEN.ENABLED=1; cartId=b6a2ce77-0880-4950-b035-bde64042746a; _scid=16b0d277-69c4-4649-9eb7-aacf33fb0eb0; _pin_unauth=dWlkPVlqRXlabVE0WmpRdFptWTJPUzAwTXpJMkxXRTJNRE10WlRZNE1tUTRNR00wTldabA; BVBRANDID=dc782732-2ebe-4fc3-bacf-f3553c2ba90d; BVImplmain_site=2036; ENV=ak-eus-t1-prod; bstc=cOgytbuHSUBJ3XXBCcQIBs; xpa=--jYu|-99OH|1sIDy|2lwWQ|3zyae|59Tck|5p0A0|5p25F|7QNwp|7Xi3l|8C3ux|9ZcI6|9jPmV|AuvWK|D4f_q|D9LOQ|EF9Bs|EL3ho|ENqC6|F6obB|FtRSv|H33MR|H67lQ|HKhPY|HRTLp|HTPms|HW-Xl|Hoe5J|I9Jw3|II82a|IVqRT|J6lpV|JOdOP|JoXRc|JvV8u|KERNb|KeAz7|MbHLZ|NOaJP|NPyyt|NbKZN|OVStb|OgGb6|PEwcJ|PHaOk|PMYXx|R79oz|RG5Bo|Ru7oD|S0hIk|Sow5W|Sq5sb|T0TXC|T4DD-|V3_qS|VBVd7|W-D6M|XDZ51|XpoJ0|YmdKw|_IueI|_J9It|_lDzX|_vHmT|_vY-K|a4fYU|aVJBH|amlzz|dQFBj|eDgDq|ep_RO|htzpo|jeBOs|kCz1y|m2qz0|mOlOu|mfKI8|njl-a|p1Ejf|rWfNO|sbXJ0|tnV6l|uBlcT|u_M4R|v-FRz|vm9yl|wI_Ba|wKkZZ|xafoR|yAFBx; exp-ck=--jYu11sIDy13zyae159Tck15p25F17QNwp17Xi3l18C3ux39ZcI619jPmV1AuvWK1D4f_q1D9LOQ2EF9Bs1EL3ho1F6obB1FtRSv1H33MR1H67lQ6HKhPY1HTPms1HW-Xl8Hoe5J1I9Jw31II82a7IVqRT1JOdOP1JoXRc1JvV8u1KERNb3KeAz71MbHLZ1NPyyt4NbKZN5OVStb1OgGb61R79oz1RG5Bo4Ru7oD1S0hIk1Sow5W1Sq5sb1T4DD-5V3_qS1XDZ511XpoJ01YmdKw1_IueI1_J9It1_vHmT1amlzz1eDgDq1ep_RO1htzpo1kCz1y1m2qz01mfKI81p1Ejf1rWfNO4sbXJ01tnV6l3uBlcT1u_M4R2v-FRz6vm9yl1wI_Ba1wKkZZ1yAFBx1; ak_bmsc=46A487EE9C06D338F0012EDFE1ADF012~000000000000000000000000000000~YAAQ2a9FQwHIhbGCAQAACVHXvRBxdjUQu86R5S3ujXHXOMr3h6Yz1t8nGx41yx+SOWdRL17ibXiwbJ5nsG8KWJTnXdS6tKfk1G9PpsTkhMHa1uS4nA5jUyRV1NV7QicNd90UIvjUVyov3Nhmn+X00xrYgRUb2z4miE3q66Xc8AF4XjCiMrj8YkUUQkAnUWsp15YJQ3YI7fX9b5/gch9PZP9nqeXwK23v4DG120qTWg0Nla32glNbjxKENqauvFcRO8RwX+0JRQxI/8WTox4qNqMV06wZc3NIU8oWJMhDhqb/jv9VFPZz1Z6bQewlqS9Aj7rKAP2reJb3gI3jqY88Z16u2O0bjSGcSxL6KhPzyWfRYiPih0uGnaenJAwgl/S5O2omXtTbRJo=; xpm=1%2B1661042380%2BS0V516wJjI2AAOb67ETj7g~%2B0; s_visit=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19225%7CMCMID%7C34697214536144180794224801759592372312%7CMCAID%7CNONE%7CMCOPTOUT-1661049670s%7CNONE%7CMCAAMLH-1661647270%7C7%7CMCAAMB-1661647270%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19232%7CvVersion%7C5.2.0; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=va6; headerType=grocery; _uetsid=782d818020d511ed9b12b31ed0dde046; _uetvid=782e629020d511edbde39f4ef7a55986; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D; walmart.nearestPostalCode=L3R9Z0; s_gnr=1661043673308-Repeat; gpv_Page=Search%3A%20broc%3A%20Grocery; cto_bundle=0hxtX185RnR6RlIwejJjV2R0Nm10SThCNURlYyUyQiUyRkVJV1JadGI0UFF3VUNsRkJ4TWxMUUQ2VzBIb3V4VVJQdHdGYjdtTTQ5bUNKWGd3aHVLSW5VS01Xb1lxdUd2RE1vcG1aUW02TWRHdko3cVN4RkklMkZsN1hMS0pNOXpJOWJIcVZUMlRyRw; authDuration={"lat":"1661043673951000","lt":"1661043673951000"}; _cs_id=e2503a21-8c83-a3f0-9f3f-e297ecbf2988.1661033248.3.1661043673.1661042337.1.1695197248874; _cs_s=6.0.0.1661045473523; TS017d5bf6=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; TS01170c9f=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; s_sq=%5B%5BB%5D%5D; seqnum=65; TS0196c61b=01538efd7cdef6bfdfd2863a269423f69963070a40b08b3881ee9ba9bcc9834554f37fdf989f452842959f722a64319526c54ede4d; bm_sv=97C9C791EC3108D91A1969E95338BEA1~YAAQFQ/QF4s5l7mCAQAABHf6vRBAwFCuEqoicWEXpYo0cb5wtzEGU38OechKpKx4r1NJqOYGYMjdTQ/617NzbXNeVc24WV0ArJtObbngdRPtV6hX60/91IMYTRBWdWjF7BRib3q3xkpZWreuHr70KAI/MtNtOmWWKFXZATfY+bJLGAooZE6fL3ruZ1JkmYJtnK+eH2q7/s9yiNKvDpQCdUhARhflhcc2Hhvg5IEYtPEhRCBc0zSGn84r91Dbe4RRnw==~1',
            'referer': 'https://www.walmart.ca/search?q=broc&c=10019',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'wm_qos.correlation_id': '87f9ae7b-028-182bdeb06be7e9,87f9ae7b-028-182bdeb06be7ac,87f9ae7b-028-182bdeb06be7ac',
        }

        params = {
            'suggestion': self.suggestions[0],
            'lang': 'en',
            'partial': 'false',
            'deliveryCatchmentId': '1061',
            'dynUserId': '8ccca502-bb83-49c3-8a59-0065615a134d',
        }

        response = requests.get(
            'https://www.walmart.ca/api/bsp/typeahead/products', params=params,
            cookies=cookies, headers=headers).json()

        products = {}

        for product in response['products']:
            products[product['id']] = Product(id=product['id'],
                                              skuIds=product['skuIds'],
                                              name=product['name'],
                                              description=product['description'],
                                              image=product['image'])

        self.products = products

    def get_price(self):
        cookies = {
            'localStoreInfo': 'eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9',
            'deliveryCatchment': '1061',
            'walmart.shippingPostalCode': 'L5V2N6',
            'defaultNearestStoreId': '1061',
            'wmt.c': '0',
            'vtc': 'S0V516wJjI2AAOb67ETj7g',
            'userSegment': '10-percent',
            'walmart.nearestLatLng': '"43.8483,-79.3349"',
            'walmart.id': '7e63d549-4f12-4e60-89a3-336858345955',
            '_gcl_au': '1.1.2070437989.1661033248',
            'DYN_USER_ID': '8ccca502-bb83-49c3-8a59-0065615a134d',
            'WM_SEC.AUTH_TOKEN': 'MTAyOTYyMDE4892TaUaERPaFJ1ZzqPQe2YtUSZTwxe8fs5K1tFPfr2rLqxfUizCyFgYibrn6+OkI9ugJVTg2wpbZtSHpeKvM4qxoO7XjG6us90cMLdpkYNcj80JF07g1vbZLKpwu7N3gj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj3q+sxGPiNWrB2amHKKiX2S42068UyLzo6DZUe4HG93fpQ2Tb7w+T0sRXSVmjJQd9Lb/SoGFgAYL9DGZ8K45WCXM/FHGZ2dCNmxWrdkwqEKrt821pAn2E5aDsnhYCCZKDAZUfaJV09dWZAaPPoL0DTkO2cN6PFGnxcmaMTzQIvEBfq2RBtC3e+zyJ8k1hTJn1bCqDbHqzyLX19PYm8H+OfNpKyn8GJqhjhOBicQkFdiGkr1eX9YGQ0laieVMoEr348=',
            'LT': '1661033249135',
            'DYN_USER_ID.ro': '8ccca502-bb83-49c3-8a59-0065615a134d',
            'pxcts': '7b57f990-20d4-11ed-b745-516c466f5543',
            '_pxvid': '7b57ee8c-20d4-11ed-b745-516c466f5543',
            '_ga': 'GA1.2.1891062393.1661033249',
            '_gid': 'GA1.2.958446820.1661033249',
            '_cs_c': '1',
            's_ecid': 'MCMID%7C34697214536144180794224801759592372312',
            'AMCVS_C4C6370453309C960A490D44%40AdobeOrg': '1',
            '__gads': 'ID=85778bf916199b20-2260cf72b9d40031:T=1661033249:S=ALNI_MbtlT-8qJfXAkD3Bg1yMwpCifvoZQ',
            '__gpi': 'UID=000008021c6d9707:T=1661033249:RT=1661033249:S=ALNI_MZjCN2tQ24WzDAw_MGJpBuvNlxZrw',
            's_cc': 'true',
            '_fbp': 'fb.1.1661033249952.1937814821',
            'kndctr_C4C6370453309C960A490D44_AdobeOrg_identity': 'CiYzNDY5NzIxNDUzNjE0NDE4MDc5NDIyNDgwMTc1OTU5MjM3MjMxMlIOCKT8r-qrMBgBKgNWQTbwAaT8r-qrMA==',
            '_4c_': '%7B%22_4c_mc_%22%3A%22dd5400b5-3ee4-4cd2-9069-dabc7628b8a5%22%7D',
            'NEXT_GEN.ENABLED': '1',
            'cartId': 'b6a2ce77-0880-4950-b035-bde64042746a',
            '_scid': '16b0d277-69c4-4649-9eb7-aacf33fb0eb0',
            '_pin_unauth': 'dWlkPVlqRXlabVE0WmpRdFptWTJPUzAwTXpJMkxXRTJNRE10WlRZNE1tUTRNR00wTldabA',
            'BVBRANDID': 'dc782732-2ebe-4fc3-bacf-f3553c2ba90d',
            'BVImplmain_site': '2036',
            'ENV': 'ak-eus-t1-prod',
            'bstc': 'cOgytbuHSUBJ3XXBCcQIBs',
            'xpa': '--jYu|-99OH|1sIDy|2lwWQ|3zyae|59Tck|5p0A0|5p25F|7QNwp|7Xi3l|8C3ux|9ZcI6|9jPmV|AuvWK|D4f_q|D9LOQ|EF9Bs|EL3ho|ENqC6|F6obB|FtRSv|H33MR|H67lQ|HKhPY|HRTLp|HTPms|HW-Xl|Hoe5J|I9Jw3|II82a|IVqRT|J6lpV|JOdOP|JoXRc|JvV8u|KERNb|KeAz7|MbHLZ|NOaJP|NPyyt|NbKZN|OVStb|OgGb6|PEwcJ|PHaOk|PMYXx|R79oz|RG5Bo|Ru7oD|S0hIk|Sow5W|Sq5sb|T0TXC|T4DD-|V3_qS|VBVd7|W-D6M|XDZ51|XpoJ0|YmdKw|_IueI|_J9It|_lDzX|_vHmT|_vY-K|a4fYU|aVJBH|amlzz|dQFBj|eDgDq|ep_RO|htzpo|jeBOs|kCz1y|m2qz0|mOlOu|mfKI8|njl-a|p1Ejf|rWfNO|sbXJ0|tnV6l|uBlcT|u_M4R|v-FRz|vm9yl|wI_Ba|wKkZZ|xafoR|yAFBx',
            'exp-ck': '--jYu11sIDy13zyae159Tck15p25F17QNwp17Xi3l18C3ux39ZcI619jPmV1AuvWK1D4f_q1D9LOQ2EF9Bs1EL3ho1F6obB1FtRSv1H33MR1H67lQ6HKhPY1HTPms1HW-Xl8Hoe5J1I9Jw31II82a7IVqRT1JOdOP1JoXRc1JvV8u1KERNb3KeAz71MbHLZ1NPyyt4NbKZN5OVStb1OgGb61R79oz1RG5Bo4Ru7oD1S0hIk1Sow5W1Sq5sb1T4DD-5V3_qS1XDZ511XpoJ01YmdKw1_IueI1_J9It1_vHmT1amlzz1eDgDq1ep_RO1htzpo1kCz1y1m2qz01mfKI81p1Ejf1rWfNO4sbXJ01tnV6l3uBlcT1u_M4R2v-FRz6vm9yl1wI_Ba1wKkZZ1yAFBx1',
            'ak_bmsc': '46A487EE9C06D338F0012EDFE1ADF012~000000000000000000000000000000~YAAQ2a9FQwHIhbGCAQAACVHXvRBxdjUQu86R5S3ujXHXOMr3h6Yz1t8nGx41yx+SOWdRL17ibXiwbJ5nsG8KWJTnXdS6tKfk1G9PpsTkhMHa1uS4nA5jUyRV1NV7QicNd90UIvjUVyov3Nhmn+X00xrYgRUb2z4miE3q66Xc8AF4XjCiMrj8YkUUQkAnUWsp15YJQ3YI7fX9b5/gch9PZP9nqeXwK23v4DG120qTWg0Nla32glNbjxKENqauvFcRO8RwX+0JRQxI/8WTox4qNqMV06wZc3NIU8oWJMhDhqb/jv9VFPZz1Z6bQewlqS9Aj7rKAP2reJb3gI3jqY88Z16u2O0bjSGcSxL6KhPzyWfRYiPih0uGnaenJAwgl/S5O2omXtTbRJo=',
            'xpm': '1%2B1661042380%2BS0V516wJjI2AAOb67ETj7g~%2B0',
            's_visit': '1',
            'AMCV_C4C6370453309C960A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C19225%7CMCMID%7C34697214536144180794224801759592372312%7CMCAID%7CNONE%7CMCOPTOUT-1661049670s%7CNONE%7CMCAAMLH-1661647270%7C7%7CMCAAMB-1661647270%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19232%7CvVersion%7C5.2.0',
            'kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster': 'va6',
            'headerType': 'grocery',
            '_uetsid': '782d818020d511ed9b12b31ed0dde046',
            '_uetvid': '782e629020d511edbde39f4ef7a55986',
            '_cs_cvars': '%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D',
            'walmart.nearestPostalCode': 'L3R9Z0',
            's_gnr': '1661043673308-Repeat',
            'gpv_Page': 'Search%3A%20broc%3A%20Grocery',
            'cto_bundle': '0hxtX185RnR6RlIwejJjV2R0Nm10SThCNURlYyUyQiUyRkVJV1JadGI0UFF3VUNsRkJ4TWxMUUQ2VzBIb3V4VVJQdHdGYjdtTTQ5bUNKWGd3aHVLSW5VS01Xb1lxdUd2RE1vcG1aUW02TWRHdko3cVN4RkklMkZsN1hMS0pNOXpJOWJIcVZUMlRyRw',
            'authDuration': '{"lat":"1661043673951000","lt":"1661043673951000"}',
            '_cs_id': 'e2503a21-8c83-a3f0-9f3f-e297ecbf2988.1661033248.3.1661043673.1661042337.1.1695197248874',
            '_cs_s': '6.0.0.1661045473523',
            'TS017d5bf6': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            'TS01170c9f': '01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274',
            's_sq': '%5B%5BB%5D%5D',
            'TS0196c61b': '01538efd7cdef6bfdfd2863a269423f69963070a40b08b3881ee9ba9bcc9834554f37fdf989f452842959f722a64319526c54ede4d',
            'seqnum': '66',
            'bm_sv': '97C9C791EC3108D91A1969E95338BEA1~YAAQFQ/QF9U5l7mCAQAAqHj6vRCZyd71w1FufC2rKL0eSiwWM0vQOgfzl+ZPww3xC+GCrQbAH6CIdKtUDdxX6/oBZ+2BNZ435+Mo24ACx1UqaWof3XBUtxaEa+1BBjAqjbOoVf34NVTZyRyZZOfqsHYWzRBjcgpdLOg5gj1Fcc/aRmTAP+19LLNI8yoftUKniCC7S1qSVTkgAfVf74lyK5U+FKTe5AFXU/zmp4TAOgz28dpWwfkxhKlGumjoSpN/zg==~1',
        }

        headers = {
            'authority': 'www.walmart.ca',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; wmt.c=0; vtc=S0V516wJjI2AAOb67ETj7g; userSegment=10-percent; walmart.nearestLatLng="43.8483,-79.3349"; walmart.id=7e63d549-4f12-4e60-89a3-336858345955; _gcl_au=1.1.2070437989.1661033248; DYN_USER_ID=8ccca502-bb83-49c3-8a59-0065615a134d; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4892TaUaERPaFJ1ZzqPQe2YtUSZTwxe8fs5K1tFPfr2rLqxfUizCyFgYibrn6+OkI9ugJVTg2wpbZtSHpeKvM4qxoO7XjG6us90cMLdpkYNcj80JF07g1vbZLKpwu7N3gj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj3q+sxGPiNWrB2amHKKiX2S42068UyLzo6DZUe4HG93fpQ2Tb7w+T0sRXSVmjJQd9Lb/SoGFgAYL9DGZ8K45WCXM/FHGZ2dCNmxWrdkwqEKrt821pAn2E5aDsnhYCCZKDAZUfaJV09dWZAaPPoL0DTkO2cN6PFGnxcmaMTzQIvEBfq2RBtC3e+zyJ8k1hTJn1bCqDbHqzyLX19PYm8H+OfNpKyn8GJqhjhOBicQkFdiGkr1eX9YGQ0laieVMoEr348=; LT=1661033249135; DYN_USER_ID.ro=8ccca502-bb83-49c3-8a59-0065615a134d; pxcts=7b57f990-20d4-11ed-b745-516c466f5543; _pxvid=7b57ee8c-20d4-11ed-b745-516c466f5543; _ga=GA1.2.1891062393.1661033249; _gid=GA1.2.958446820.1661033249; _cs_c=1; s_ecid=MCMID%7C34697214536144180794224801759592372312; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; __gads=ID=85778bf916199b20-2260cf72b9d40031:T=1661033249:S=ALNI_MbtlT-8qJfXAkD3Bg1yMwpCifvoZQ; __gpi=UID=000008021c6d9707:T=1661033249:RT=1661033249:S=ALNI_MZjCN2tQ24WzDAw_MGJpBuvNlxZrw; s_cc=true; _fbp=fb.1.1661033249952.1937814821; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYzNDY5NzIxNDUzNjE0NDE4MDc5NDIyNDgwMTc1OTU5MjM3MjMxMlIOCKT8r-qrMBgBKgNWQTbwAaT8r-qrMA==; _4c_=%7B%22_4c_mc_%22%3A%22dd5400b5-3ee4-4cd2-9069-dabc7628b8a5%22%7D; NEXT_GEN.ENABLED=1; cartId=b6a2ce77-0880-4950-b035-bde64042746a; _scid=16b0d277-69c4-4649-9eb7-aacf33fb0eb0; _pin_unauth=dWlkPVlqRXlabVE0WmpRdFptWTJPUzAwTXpJMkxXRTJNRE10WlRZNE1tUTRNR00wTldabA; BVBRANDID=dc782732-2ebe-4fc3-bacf-f3553c2ba90d; BVImplmain_site=2036; ENV=ak-eus-t1-prod; bstc=cOgytbuHSUBJ3XXBCcQIBs; xpa=--jYu|-99OH|1sIDy|2lwWQ|3zyae|59Tck|5p0A0|5p25F|7QNwp|7Xi3l|8C3ux|9ZcI6|9jPmV|AuvWK|D4f_q|D9LOQ|EF9Bs|EL3ho|ENqC6|F6obB|FtRSv|H33MR|H67lQ|HKhPY|HRTLp|HTPms|HW-Xl|Hoe5J|I9Jw3|II82a|IVqRT|J6lpV|JOdOP|JoXRc|JvV8u|KERNb|KeAz7|MbHLZ|NOaJP|NPyyt|NbKZN|OVStb|OgGb6|PEwcJ|PHaOk|PMYXx|R79oz|RG5Bo|Ru7oD|S0hIk|Sow5W|Sq5sb|T0TXC|T4DD-|V3_qS|VBVd7|W-D6M|XDZ51|XpoJ0|YmdKw|_IueI|_J9It|_lDzX|_vHmT|_vY-K|a4fYU|aVJBH|amlzz|dQFBj|eDgDq|ep_RO|htzpo|jeBOs|kCz1y|m2qz0|mOlOu|mfKI8|njl-a|p1Ejf|rWfNO|sbXJ0|tnV6l|uBlcT|u_M4R|v-FRz|vm9yl|wI_Ba|wKkZZ|xafoR|yAFBx; exp-ck=--jYu11sIDy13zyae159Tck15p25F17QNwp17Xi3l18C3ux39ZcI619jPmV1AuvWK1D4f_q1D9LOQ2EF9Bs1EL3ho1F6obB1FtRSv1H33MR1H67lQ6HKhPY1HTPms1HW-Xl8Hoe5J1I9Jw31II82a7IVqRT1JOdOP1JoXRc1JvV8u1KERNb3KeAz71MbHLZ1NPyyt4NbKZN5OVStb1OgGb61R79oz1RG5Bo4Ru7oD1S0hIk1Sow5W1Sq5sb1T4DD-5V3_qS1XDZ511XpoJ01YmdKw1_IueI1_J9It1_vHmT1amlzz1eDgDq1ep_RO1htzpo1kCz1y1m2qz01mfKI81p1Ejf1rWfNO4sbXJ01tnV6l3uBlcT1u_M4R2v-FRz6vm9yl1wI_Ba1wKkZZ1yAFBx1; ak_bmsc=46A487EE9C06D338F0012EDFE1ADF012~000000000000000000000000000000~YAAQ2a9FQwHIhbGCAQAACVHXvRBxdjUQu86R5S3ujXHXOMr3h6Yz1t8nGx41yx+SOWdRL17ibXiwbJ5nsG8KWJTnXdS6tKfk1G9PpsTkhMHa1uS4nA5jUyRV1NV7QicNd90UIvjUVyov3Nhmn+X00xrYgRUb2z4miE3q66Xc8AF4XjCiMrj8YkUUQkAnUWsp15YJQ3YI7fX9b5/gch9PZP9nqeXwK23v4DG120qTWg0Nla32glNbjxKENqauvFcRO8RwX+0JRQxI/8WTox4qNqMV06wZc3NIU8oWJMhDhqb/jv9VFPZz1Z6bQewlqS9Aj7rKAP2reJb3gI3jqY88Z16u2O0bjSGcSxL6KhPzyWfRYiPih0uGnaenJAwgl/S5O2omXtTbRJo=; xpm=1%2B1661042380%2BS0V516wJjI2AAOb67ETj7g~%2B0; s_visit=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19225%7CMCMID%7C34697214536144180794224801759592372312%7CMCAID%7CNONE%7CMCOPTOUT-1661049670s%7CNONE%7CMCAAMLH-1661647270%7C7%7CMCAAMB-1661647270%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19232%7CvVersion%7C5.2.0; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=va6; headerType=grocery; _uetsid=782d818020d511ed9b12b31ed0dde046; _uetvid=782e629020d511edbde39f4ef7a55986; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D; walmart.nearestPostalCode=L3R9Z0; s_gnr=1661043673308-Repeat; gpv_Page=Search%3A%20broc%3A%20Grocery; cto_bundle=0hxtX185RnR6RlIwejJjV2R0Nm10SThCNURlYyUyQiUyRkVJV1JadGI0UFF3VUNsRkJ4TWxMUUQ2VzBIb3V4VVJQdHdGYjdtTTQ5bUNKWGd3aHVLSW5VS01Xb1lxdUd2RE1vcG1aUW02TWRHdko3cVN4RkklMkZsN1hMS0pNOXpJOWJIcVZUMlRyRw; authDuration={"lat":"1661043673951000","lt":"1661043673951000"}; _cs_id=e2503a21-8c83-a3f0-9f3f-e297ecbf2988.1661033248.3.1661043673.1661042337.1.1695197248874; _cs_s=6.0.0.1661045473523; TS017d5bf6=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; TS01170c9f=01538efd7c515dbb46d5171e91f4ff5dda600985cf8d69810a395b7a64d8daf3a4f30148d8d338d638fcdfdd240ed1ada1801cb274; s_sq=%5B%5BB%5D%5D; TS0196c61b=01538efd7cdef6bfdfd2863a269423f69963070a40b08b3881ee9ba9bcc9834554f37fdf989f452842959f722a64319526c54ede4d; seqnum=66; bm_sv=97C9C791EC3108D91A1969E95338BEA1~YAAQFQ/QF9U5l7mCAQAAqHj6vRCZyd71w1FufC2rKL0eSiwWM0vQOgfzl+ZPww3xC+GCrQbAH6CIdKtUDdxX6/oBZ+2BNZ435+Mo24ACx1UqaWof3XBUtxaEa+1BBjAqjbOoVf34NVTZyRyZZOfqsHYWzRBjcgpdLOg5gj1Fcc/aRmTAP+19LLNI8yoftUKniCC7S1qSVTkgAfVf74lyK5U+FKTe5AFXU/zmp4TAOgz28dpWwfkxhKlGumjoSpN/zg==~1',
            'origin': 'https://www.walmart.ca',
            'referer': 'https://www.walmart.ca/search?q=broc&c=10019',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'wm_qos.correlation_id': '87f9ae7b-028-182bdeb06be7e9,87f9ae7b-028-182bdeb06be7ac,87f9ae7b-028-182bdeb06be7ac',
        }

        json_data = {
            'lang': 'en',
            'pricingStoreId': '1061',
            'availabilityStoreId': '1061',
            'products': [{'productId': product.id, 'skuIds': product.skuIds} for product
                         in self.products.values()],
            'fsa': 'L5V'
        }

        response = requests.post(
            'https://www.walmart.ca/api/bsp/typeahead/pnos', cookies=cookies,
            headers=headers, json=json_data).json()

        for product in response:
            self.products[product["productId"]].price = product["priceInfo"]["price"]

    def search(self, term):
        self.term = term
        self.get_suggestions()
        self.get_products()
        self.get_price()
