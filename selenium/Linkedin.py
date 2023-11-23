from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.add_argument("--window-size=500,500")
driver = webdriver.Chrome(options=options)
url='https://www.linkedin.com/in/johndanes/'
driver.get(url)

# Using explicit wait for the button element to be clickable

def clickFunc(path):
    try:
        folder = WebDriverWait(driver,2).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        print(folder.text)
        folder.click()
    except Exception as e:
        pass
        # print(f"error in {path}")
        # print(f"Exception: {e}")

def inputFunc(path,text):
    try: #//*[@id="session_key"]
        email_field = WebDriverWait(driver,2).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        text_to_paste = text
        email_field.send_keys(text_to_paste)
    except Exception as e:
        pass
        # print(f"error in {path}")
        # print(f"Exception: {e}")

def detailfet(path):
    try: 
        namefetch = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        name_text = namefetch.text  # Store the text content in a variable
        print(name_text)  # Print or use the fetched text
        return name_text
    except Exception as e:
        print("Error in Details")
        return 'error'
        # print(f"Exception: {e}")

def signinlingke():
    signuplist=['//*[@id="main-content"]/div/form/p/button','//*[@id="public_profile_contextual-sign-in"]/div/section/div/div/div/div[1]/button','//*[@id="public_profile_contextual-sign-in"]/div/section/div/div/p/a']
    emailist=['//*[@id="session_key"]','//*[@id="email-or-phone"]','//*[@id="main-content"]/div[1]/div/form/div[1]/div[1]/div/div','//*[@id="public_profile_contextual-sign-in_sign-in-modal_session_key"]']
    passlist=['//*[@id="public_profile_contextual-sign-in_sign-in-modal_session_password"]','//*[@id="session_password"]']
    signclicklist=['//*[@id="main-content"]/div[1]/div/form/div[2]/button','//*[@id="public_profile_contextual-sign-in_sign-in-modal"]/div/section/div/div/form/div[2]/button']

    print("Clicking on Signup")
    for a in signuplist:
        clickFunc(a)

    print('EmailTime')
    for b in emailist:
        email=''
        inputFunc(b,email)

    print('PassTime')
    for c in passlist:
        email=''
        inputFunc(c,email)

    for d in signclicklist:
        clickFunc(d)
signinlingke()

DetailsDic={}
namepath='//*[@id="ember32"]/h1' #name
adresspath='//*[@id="ember29"]/div[2]/div[2]/div[2]/span[1]' #Address
companypath='//*[@id="ember29"]/div[2]/div[2]/ul/li[1]/button' # Company
urls=["https://www.linkedin.com/in/monica-siverio-sphr-4a868077/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/johndanes/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/ken-diener-dht-a27bb730/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/uzairshaikh96/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/hunter-little-5b071285/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/jonathan-espinoza-573219ba/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/christian-cruz-215a95217/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/david-boroughs-73117363/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/theodore-damon-1b9a4958/?lipi=urn%3Ali%3Apage%3Aorganization_admin_admin_analytics_followers%3Bad4ca055-ffbb-4674-8024-10f0b04dae15","https://www.linkedin.com/in/siegurd-rust-96ba6947/","https://www.linkedin.com/in/marcos-topolanski-quintero/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B5V2jrlfSRkae5ZkNcBGYig%3D%3D","https://www.linkedin.com/in/waynehutcherson/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B5V2jrlfSRkae5ZkNcBGYig%3D%3D","https://www.linkedin.com/in/ben-glazier-a15b3bb8/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B5V2jrlfSRkae5ZkNcBGYig%3D%3D","https://www.linkedin.com/in/charles-pauly-51a620110/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/russ-puhr-aa6169ab/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/chelsey-jimenez-383811216/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/ronnie-allen-3323358b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/javier-j-mendoza-554502a0/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/astik-shukla-780551160/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/rudra-pratap11/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/kimberlee-gaddis-78325046/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGixU0oIeTeq881ym2FSAfA%3D%3D","https://www.linkedin.com/in/noomen-chaabene-923b66198/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jamie-ikenberry-9b7157216/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/deodatta-sontakke-1654a1137/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/ian-cavanagh-tifiree-mifsm-mafdi-66aa2244/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/liam-o%E2%80%99loughlin-002422ba/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/guy-t-robinson-psp-cpl-71631412/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jon-miller-072883143/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/brian-mcfall-990b71b2/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/hardwaresolutions/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/david-eli-7a348b1b5/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/david-eli-7a348b1b5/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/reina-f-bb829929/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/armando-orozco-88aaa01a1/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/isaac-elizondo/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/chase-ricamore-41108663/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jimmy-klawetter-835a46b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/alex-smith-128b09210/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/nancytolani/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/tamara-jones-049b57144/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/emmanuel-magezi-b965a318b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/kris-sims-7090378a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jo-washington/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/david-torrentt-8828b2126/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/claudia-carroll-aa2326131/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/cian-kelleher/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jeremy-diener-613b3a122/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/thomas-george-palatty/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/paul-bell-1b143389/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/samantha-balmes-23a93848/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/juliadunlevy/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/veronica-guerrero-37ba45148/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/amy-e-salmeron-csi-cdt-49b9133/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/victor-alejandro-leon/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/nesar-ahmad-pmp%C2%AE-012217125/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jack-cox-76507417a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/matt-banham-2b61386b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/michael-shone-6804981a0/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/harry-watt-9a86101b6/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/debbie-day-02928610b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/liz-gardu%C3%B1o-93236320b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jeffrey-matherly-a789b915a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jared-lehr-03792ab9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/adcoinstallers/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/benjibolickthedoordork/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/roger-diener-a92a9712b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/prince-surve-7a6450186/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/lucelle-diener-aa0706196/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/peter-sedgwick-99674517/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jonas-devita-7955b01/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/kaitlyn-summerfield-74b88611a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/chintansalvi/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/ryan-dorr-norwalk-iowa/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/roger-diener-b09141b8/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/shannon-keever-63a369149/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jonathan-whittam-71701381/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/sam-gale-255b991b3/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/bethany-cuff-21a92b193/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/beverley-walker-476a0a46/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/danny-mcardle-0a9423246/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/john-sidebottom-18b70679/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/ross-murphy-22646497/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/tom-ely-0a9058b7/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/dave-burkill-6583b0109/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/connor-horne-4b68421a3/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/john-draper-661262215/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/adam-s-425b29152/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/nick-smith-05bb342b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/nickingrem/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/jack-garrard-55a26a1b1/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/richardosbond/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/kaine-mistry-1b1988210/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/steve-carr-4532a8166/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/bryony-fellows-7aba9112a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/david-may-4415963b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/sam-cox-3aba3a201/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/scot-jerram-25574b158/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BGrNpTsbqRzSH32P7HEWpPw%3D%3D","https://www.linkedin.com/in/carl-p-brown-42a56838/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/mostafa-omar-67888a257/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/thomas-g-4746b412a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/wes-diener-3510b231/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/nicole-casa-cfdai-dsi-qfdi-qfdt-505438194/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/patrick-redmond-sr-recruiter/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/sarah-gentry-730/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/lou-andruzzi/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/adamericrichards/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/cmstaley/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/ben-zuverink-20832241/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/gizelle-williams-98b36419/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/catherine-wong-899102227/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bo30Ssq1bQk%2Bj2o0qPXcVWg%3D%3D","https://www.linkedin.com/in/jes%C3%BAs-ord%C3%B3%C3%B1ez-merlos-29b76426/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/david-d-75005a123/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/sam-pound-4233a0173/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/jacqueline-litza/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/joelleonardmakersmaker/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/steve-stanger-5aaa191b6/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/laharika-bowinpally-955033222/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/martin-palfrey-3a3a13255/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/giorgis-simakou-b6ba231b7/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/claire-lowes-98819644/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/ronnell-keys-2a362719a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/jordan-flint-1a689a116/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/roopitha-angeline-1844b419b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/tim-evershed-016303223/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/seifeddin-wifatti-2b24891b0/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/david-oldfield-3644a119/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/gnana-somesh-velagala-245096208/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/ciara-doherty-374293211/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/david-wright-949910116/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/matthew-jackson-2624551a9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/scott-martin-8b4a80b0/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/john-padian-9b4201102/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/dominic-giannini-658594287/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/francisco-gutierrez-23a3a0177/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/curtis-holt-1920b2179/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/tim-hunt-pdh/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/frank-garza-11b1521a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/jo-davies-b7218316b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/alwin-philip/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/kimberley-burgess-2042a6191/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/active-fire-door-products-7b2873207/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/cathy-browning-63475018/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/hutchinsgary/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/hollyjunesmith/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BPB0OlmmUR0%2B1u0l9OqXTFQ%3D%3D","https://www.linkedin.com/in/simongoddard/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bu%2BgJnHrZSsGEjKrKTKq4vg%3D%3D","https://www.linkedin.com/in/george-allen-200a0a199/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3Bu%2BgJnHrZSsGEjKrKTKq4vg%3D%3D","https://www.linkedin.com/in/marcusddixon/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BlUOwAWVtSHKqaHWbnuCmNQ%3D%3D","https://www.linkedin.com/in/dean-asling-830a6550/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BlUOwAWVtSHKqaHWbnuCmNQ%3D%3D","https://www.linkedin.com/in/ansu-mary-alex-5ab193211/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BlUOwAWVtSHKqaHWbnuCmNQ%3D%3D","https://www.linkedin.com/in/jono-mccall-555332115/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BlUOwAWVtSHKqaHWbnuCmNQ%3D%3D","https://www.linkedin.com/in/georgiagreen-bradbury/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BlUOwAWVtSHKqaHWbnuCmNQ%3D%3D","https://www.linkedin.com/in/imogen-taylor-782ba2225/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3BlUOwAWVtSHKqaHWbnuCmNQ%3D%3D","https://www.linkedin.com/in/marilyn-milorey-b255ba67/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/jake-moretta-527076b6/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/lauren-walker-30240571/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/john-ahern-049617262/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/norman-simpson-50aa8b210/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/scott-redfern-5390a193/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/jacob-clarke-3594301bb/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/stephan-van-wyk-227781257/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/rebecca-hawkins-070902233/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/paul-andrew-r-019b5390/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/scott-swain-12730117b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/daniel-kardos-9b432a112/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/antony-allen-87217929/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/jack-morris-8634351b0/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/dominique-thistleton-98833527/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/ashlin-southon-46021b119/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/daniel-hopkinson-83612359/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/jessica-goldman-a513a2105/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/judith-calisti-90239b230/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/craig-newbound-57960a132/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/daniel-gilchrist-aifsm-dipfd-868269132/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/elisha-rawlins-719b6b1a9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/joana-mwakasungula-mrics-5057a11b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/mick-hall-197292239/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/abelat/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/matt-bates-5621901a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/alex-holbrook-17b0a7207/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/craig-blunt-doorsets/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/alexander-cook-78ab4696/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/rohan-shirodkar-pmp-41805820/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/daradavis03/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/kamil-frodyma-316457115/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/noelle-abdel-massih-ultimaten/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/darren-slater-gifiree-cfpa-e-dip-tc-15b111149/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/donald-frederic-comstock-ii-967103295/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/rizwan-masood-5885291bb/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/brett-pavel-70a18316a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/kathryn-van-der-merwe-b4a56b254/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/nbamford/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/jasonschroederelevatingconstruction/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/chris-touchberry/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/adryan-martinelli-8436068b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/leeodess/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/blake-edwards-b977aa90/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/wade-bergeron-217234101/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/samlsutherland-mba-09879795/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/mark-a-johnston-a71a406/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/hallrb/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/mary-brezinski-946941b8/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/robert-volpe-leed-ap-csi-cdt-4b2479151/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/martin-p-2a204438/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/ryan-flaherty-hamilton-621432161/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3By%2ByrKUttS561ZCJFKm4TFg%3D%3D","https://www.linkedin.com/in/hayden-abrevaya/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/rory-king-66b01a172/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/everett-rosette-28021817/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/mark-scollen-585a3ba1/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/tom-shard-338822222/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/yordanka-perez-9b75988a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/katelynn-german-93b67a116/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D","https://www.linkedin.com/in/lorigreeneahc/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company_admin%3B9hrp9HQ%2FR0aM19J4w47qaQ%3D%3D"]

for a in urls:
    try:
        driver.get(a)
        name=detailfet(namepath)
        address=detailfet(adresspath)
        company=detailfet(companypath)

        if name and address and company =='error':
            signinlingke()
            driver.get(a)
            name=detailfet(namepath)
            address=detailfet(adresspath)
            company=detailfet(companypath)           
        DetailsDic[a]=(name,address,company)
    except:
        print("\n \n")
        print(DetailsDic.items())

        file_path = "dict_data.txt"

        # Open the file in write mode and save key-value pairs
        with open(file_path, 'w') as file:
            for key, value in DetailsDic.items():
                file.write(f"{key}: {', '.join(map(str, value))}\n")
        
        print(f"\n\n\n Error at{a}")
