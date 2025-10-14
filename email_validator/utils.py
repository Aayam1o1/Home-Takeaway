import re
import dns.resolver
import smtplib

def is_valid_email_format(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def check_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return len(answers) > 0
    except Exception:
        return False

def check_smtp(email):
    try:
        domain = email.split("@")[1]
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx = str(mx_records[0].exchange)
        server = smtplib.SMTP(timeout=5)
        server.connect(mx)
        server.quit()
        return True
    except Exception:
        return False

def check_spf(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if "v=spf1" in rdata.to_text():
                return True
        return False
    except Exception:
        return False

def check_dkim(domain):
    try:
        selector = "default"
        answers = dns.resolver.resolve(f"{selector}._domainkey.{domain}", 'TXT')
        return len(answers) > 0
    except Exception:
        return False

def check_dmarc(domain):
    try:
        answers = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
        return len(answers) > 0
    except Exception:
        return False
