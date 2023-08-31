from rsa import PublicKey
from telethon._impl.crypto.rsa import (
    PRODUCTION_RSA_KEY,
    TESTMODE_RSA_KEY,
    compute_fingerprint,
    encrypt_hashed,
)


def test_fingerprint_1() -> None:
    fp = compute_fingerprint(PRODUCTION_RSA_KEY)
    assert fp == -3414540481677951611


def test_fingerprint_2() -> None:
    fp = compute_fingerprint(TESTMODE_RSA_KEY)
    assert fp == -5595554452916591101


def test_rsa_encryption() -> None:
    key = PublicKey(
        n=25342889448840415564971689590713473206898847759084779052582026594546022463853940585885215951168491965708222649399180603818074200620463776135424884632162512403163793083921641631564740959529419359595852941166848940585952337613333022396096584117954892216031229237302943701877588456738335398602461675225081791820393153757504952636234951323237820036543581047826906120927972487366805292115792231423684261262330394324750785450942589751755390156647751460719351439969059949569615302809050721500330239005077889855323917509948255722081644689442127297605422579707142646660768825302832201908302295573257427896031830742328565032949,
        e=65537,
    )
    result = encrypt_hashed(
        bytes.fromhex(
            "955ff5a9081a8e635f5743de9b00000004453dc27100000004622f1fcb000000f7a81627bbf511fa4afef71e94a0937474586c1add9198dda81a5df8393871c8293623c5fb968894af1be7dfe9c7be813f9307789242fd0cb0c16a5cb39a8d3e"
        ),
        key,
        bytes.fromhex(
            "12270000635593b03fee033d0672f9afddf9124de9e77df6251806cba93482e4c9e6e06e7d44e4c4baae821aff91af44789689faaee9bdfc7b2df8c08709afe57396c4638ceaa0dc30114f82447e81d3b53edc423b32660c43a5b8ad057b64500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007dada0920c4973913229e0f881aec7b9db0c392d34f52fb0995ea493ecb4c09daaf68fe9554ec7a59c03e4035952b220b47a8d06aad71134110d8c44948901f8"
        ),
    )
    assert result == bytes.fromhex(
        "c6d211349fc10cda6983276250b09f4be9b39f533b5d314b732b51a6dd72234dab4224209992c894e0e4c9f30249f1dbbd1630a27b98f2f92a53c00baabbd46f380bd35f417e5ec2edb43f7644b5c81af011d736eb369265e848b553ae5e6350dd5695efc72bde0e35f3c3fc827b91eb97cf1efdbff12269b9c33f81645adebc89ed167edc19d285237a754bf629aa358ed08498863b2aec8b7139001627bbe8bdef239474a5a43e664d278f39e72d694a206d7b838fd40868a71c4bfbffa38b7679faa502b7795cbe5ae1bd05ca7eb01ff5b05107265fd39bd5b4e19d392b735a3b0b5b21473062981bff86ff9084a7b594775e3127c05fd454e19f794a4ab4"
    )
