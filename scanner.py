import socket

tinta = "scanme.nmap.org"
# Scanăm porturile 20-85 (ca să nu stăm o zi întreagă)
porturi = range(20, 86)


def grab_banner(ip, port):
    """Funcția asta face treaba grea: se conectează și trage banner-ul."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))

        # Trimitem o cerere simplă
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode("utf-8", errors="ignore")
        s.close()
        return banner
    except:
        return "Nu s-a putut captura banner-ul."


print(f"[*] Începem scanarea inteligentă pe {tinta}...")

for port in porturi:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    rezultat = s.connect_ex((tinta, port))

    if rezultat == 0:
        print(f"[+] Portul {port} este DESCHIS!")
        # AICI E LOGICA: Dacă e deschis, rulează funcția de sus!
        banner = grab_banner(tinta, port)
        print(f"    -> Banner capturat: {banner.strip()}")
    s.close()

print("[*] Scanare finalizată, queen.")
