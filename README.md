# NC_sql
用友NC pagesServlet SQL注入致RCE  

**需要安装支持库**  
pip install requests  

python yongyou_fileup.py -h                                         

                                          .-') _
                                     ( OO ) )
          ,--.   ,--..-'),-----. ,--./ ,--,'  ,----.      ,--.   ,--..-'),-----.  ,--. ,--.
           \  `.'  /( OO'  .-.  '|   \ |  |\ '  .-./-')    \  `.'  /( OO'  .-.  ' |  | |  |
         .-')     / /   |  | |  ||    \|  | )|  |_( O- ) .-')     / /   |  | |  | |  | | .-')
        (OO  \   /  \_) |  |\|  ||  .     |/ |  | .--, \(OO  \   /  \_) |  |\|  | |  |_|( OO )
         |   /  /\_   \ |  | |  ||  |\    | (|  | '. (_/ |   /  /\_   \ |  | |  | |  | | `-' /
         `-./  /.__)   `'  '-'  '|  | \   |  |  '--'  |  `-./  /.__)   `'  '-'  '('  '-'(_.-'
           `--'          `-----' `--'  `--'   `------'     `--'          `-----'   `-----'

usage: yongyou_fileup.py [-h] [-u URL] [-f FILE]  

用友NC pagesServlet SQL注入致RCE漏洞 

optional arguments:  
  -h, --help            show this help message and exit  
  -u URL, --url URL     添加url信息  
  -f FILE, --file FILE  添加txt文件  

example:  
    python3 yongyou_fileup.py -u http://xxxx.xxxx.xxxx.xxxx  
    python3 yongyou_fileup -f x_url.txt  
