from email.utils import formataddr
from email.utils import parseaddr
format_addr = formataddr(('han','junqiang_han@163.com'))

print(format_addr)

parse_addr = parseaddr(format_addr)
print(parse_addr)
