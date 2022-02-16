import re

text = """
# My first header

## Nec sic igni ad ad aventi

Lorem markdownum quantumque nunc, fine superi sagittis, haut regalis attollo,
ora inferius, mensor deam? Sedili quoque tauri. Quo limite ducem.

1. Arva fecit partes tosta
2. Insignia est ausae ut ut ait
3. O summa saepe

Sic ipsos, Phlegethontide nisi poterat neque quos tum partes rapitur. Filius
utraque: glande, ut exiles terram fiducia coeunt. Et caelo legit multis,
plangorem altoque; et iamque nec. Sanguine corpora prora quicquid insolida in
Parin: stupet est posses nos mater temptat, gemit num.

# My second header

## Primordia metuam his dixerat talaria cognoscenda

Lorem markdownum revulsum dilexit contra. Qui seu supplex Themis profuit quoque
Hyperionis, omnibus aesculus signa medendi. Aspiciunt rigidique finibus ducunt
postquam, huic postera lignum, properent.

- Nostro purgamina capitque longis
- Virtus suo moenibus
- Byblida longum pudibunda referre
- Via in ab vulneribus petita mirantur quamquam
- Et vela
- Nondum sacer meminisse Dircen novas dumque
"""

# didn't work
# r = re.compile(r"r"(?:^|\s)(?:[#]\ )(.*\n+##\ ([^#]*\n)+)"")
# print(r.findall(text))

def findHeader(search):
    r = re.compile(r"(?<!#)# " + search + r"(?s)(?:(?!(?<!#)# ).)+")
    return(r.findall(text))

# def findHeader(search):
#     r = re.compile(r"(?<!#) " + search + r"(?s)(?:(?!(?<!#) ).)+")
#     return(r.findall(text))


print(findHeader("My second header"))