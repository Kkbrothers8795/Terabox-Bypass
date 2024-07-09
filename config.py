import os
import logging
import re
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

my_cookie = "csrfToken=GHCr5c7PG7m-uNmwgZMs_rTm; browserid=IpOTkn3sUXflH137gkjAABKPpYQPOkWv7DF2TkYb-z90IFGy4K3S4fbqSHw=; lang=en; __bid_n=1904cc18665ad49a7a4207; __stripe_mid=59251633-d0b6-45e9-8f1e-60eb717f07333c544e; ndus=YvV4We4teHuiGZaml4vV_hxd2Xil7cVxPm0uO_da; _ga=GA1.1.1388011841.1719274827; ndut_fmt=EDB00A9D4747BEC087471B328D59C6E3DCD4FF1767309886F4D251A26E5E492B; ab_sr=1.0.1_ODIxYzM1Y2I2ZjM1ZTI4YmEwZDIwOTBiMTYzZmViYWRkMGQ4ODg3ZjU1MjZlZDFlNTNhNmYxNWQ0ZTcyYjQ2YTA3YmRhODcxZDFhNGUzYTQ2ODFjMjUzOWI1NjY1MDEwMWQxZDZmNmY4NTg3ZmQ4YzNkZjgxMmViMDBiNzBmMDk5NTIxODJiOTkyOTA3OTdiNzgxZTA3NGZlNzgzNjJjMg==; ab_ymg_result={"data":"14b799cd8265d59b13c8fd5c13908d8052bad7a70028faba24081a57260c043eba5845dc5d08ddb1b0745982838c1d9555586453b73aa58ce5e10dfad9efe19c822c345a9fe8409a95942660244e20ff98fc8835a7b9cfa798b0e1afaa1103be3a7208e24410e0dabb90f7b0b41cffa2d88b904a65d513e7e79f08ed2d0d7de1","key_id":"66","sign":"96e98196"}; _ga_06ZNKL8C2E=GS1.1.1720499435.4.1.1720499493.2.0.0"
my_headers = "www.1024terabox.com"
session_string = "BQAOHLsAODdOX7Zon__Oc_e8JaSR9Xk8QvcDdqatwgZkIbJhM_Hozgz_SwJ6rBatjI_WwVsdDigWE_2vJakbomh1x6rQA_24v0ew2J_kT2OOVYLhkOc-lKeMAK3IjK9P7mrQ1QaXyawuGEEDxUx-r7tfZix8YljjxR8-VqMh4qQojFC3kO_UcArAUAbBffHn6HvTG8fCEMsJXYzid9gPaQEHibz5RBpTa-qWIRwkPrLE4U-Hfq9BqoUpNbck5iiaJmTwZZpJMCM4YX5-5P-M6jfYdPZhOX2JY7wz_bx7Q0AMvCIPgA1hVKKFYcGpoM5PVOFbyYi0LFw1CjKXW8N7HoheDr5YeAAAAAFsXii3AA"
allowed_groups = "-1001478442561"  # added random group id to avoid NoneType error
# allowed_groups = ["-123232ZCVZB"] or ["121222xxx", "123456xxx"]
owner_id = "754495556"

try:
    my_cookie = eval(my_cookie)
    my_headers = eval(my_headers)
    allowed_groups = eval(allowed_groups)
except Exception as e:
    logger.error(f"Error parsing env variables: {e}")


def extract_links(message):
    # fetch all links
    try:
        url_pattern = r'https?://\S+'
        matches = re.findall(url_pattern, message)

        return matches
    except Exception as e:
        logger.error(f"Error extracting links: {e}")
        return []
