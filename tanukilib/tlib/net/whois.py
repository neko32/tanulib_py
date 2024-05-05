from typing import Optional, Dict
from tlib.core import exec_cmd

def whois(domain:str) -> Optional[Dict[str, str]]:
    """Execute whois. If not found, None is returned"""
    retcode, stdout, _ = exec_cmd(["whois", domain])
    if retcode != 0:
        return None
    
    return {}
    