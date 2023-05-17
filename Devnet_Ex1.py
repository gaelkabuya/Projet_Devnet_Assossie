
#On accede au fichier show_IP_bgp_summ



from __future__ import print_function, unicode_literals

with open("show_ip_bgp_summ.txt") as f:
    fichier = f.read()

fichier = fichier.splitlines()

Ligne1 = fichier[0]
as_number = Ligne1.split()[-1]
print("Le numero Local AS est : {}".format(as_number))

derniere_ligne = fichier[-1]
peer_ip = derniere_ligne.split()[0]
print("L'addresse IP BGP Peer est : {}".format(peer_ip))
