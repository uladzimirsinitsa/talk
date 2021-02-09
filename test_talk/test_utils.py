
from utils import simple_slug_generator


def test_simple_slug_generator():
    assert simple_slug_generator('20 "free spins no deposit at bitStarz') == "20-free-spins-no-deposit-at-bitstarz"
    assert simple_slug_generator('Gambling Addiction Stories #19') == "gambling-addiction-stories-19"
    assert simple_slug_generator('Top 3 Online-Casinos with UKGC license') == "top-3-online-casinos-with-ukgc-license"
    assert simple_slug_generator('Top 3 Online--Casinos with UKGC license') == "top-3-online-casinos-with-ukgc-license"
    assert simple_slug_generator('Top 3 Online--Casinos with UKGC license ') == "top-3-online-casinos-with-ukgc-license"


