import re


def fun(email):
    try:
        username, rest = email.split('@')
        website, extension = rest.split('.')
    except ValueError:
        return False
    
    if not re.match(r'^[a-zA-Z0-9._-]+$', username):
        return False
    
    if not re.match(r'^[a-zA-Z0-9]+$', website):
        return False
    
    # Проверяем расширение
    if not re.match(r'^[a-zA-Z]+$', extension) or len(extension) > 3:
        return False
    
    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
