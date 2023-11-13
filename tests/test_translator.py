from retailwind.translator import Translator


def test_html(default_compiled_css):
    tr = Translator(compiled=default_compiled_css)
    r = tr.html(
        """<div class="alo ari asf">
    <div class="gx lx tw yr yz zc abw cbb cbh cbp ccr">
            <button type="button" class="adp ajr ard arp awc awg bah bbn bis boy boz bpb bpk">Button text</button>
            <button type="button" class="adp ajr ard arp awa awg bah bbn bis boy boz bpb bpk">Button text</button>
            <button type="button" class="adu ajr are arq awa awg bah bbn bis boy boz bpb bpk">Button text</button>
            <button type="button" class="adu ajr arf arv awa awg bah bbn bis boy boz bpb bpk">Button text</button>
            <button type="button" class="adu ajr arg arw awa awg bah bbn bis boy boz bpb bpk">Button text</button>
</div>
    </div>"""
    )
    print(r)
