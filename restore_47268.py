import json
import re

KO_HTML_47268 = """<div style="text-align: justify;">국내 대중 미술의 선호도는 카페 인테리어를 살펴보면 대강 보인다. 작년 가을에는 앙리 마티스(Henri Matisse, 1869~1954)와 데이비드 호크니(David Hockney, 1937~ )가 자주 보였다. 미술에는 관심이 없지만 한국에 유행하는 카페투어에 승선하는 사람이라면 그림이 눈에 익다 못해 '도대체 어떤 그림이길래 여기저기 다 붙어있어?'라며 작가 이름 한 번 쯤은 살펴봤을지도.</div>
<div><br></div>
<div style="text-align: justify;">작년 2019년에 서울시립미술관에서 열린 데이비드 호크니의 전시를 보고 온 친구는 호크니를 "미친놈!"이라며 흥분했다. 대표작이라면서 A Bigger Splash(1967)을 보여주었는데, 당시 모네(Claude Monet, 1840~1926)로 관심이 복귀했던 터라, 딱히 흥미가 가지는 않았다. 캔버스의 구역을 정확히 나누는 A Bigger Splash(1967)와 정형화의 정 반대편에 선 모네는 반대 위치이지 않은가.</div>
<div>&nbsp;</div>
<div>
   <div class="cheditor-caption-wrapper" style="text-align: center;">
      <figure class="cheditor-caption" style="margin: 0px; border: 1px solid rgb(204, 204, 204); border-image: none; width: 660px; display: inline-block; background-color: #f0f0f0;">
         <img style="width: 660px; height: 668px;" alt="A Bigger Splash" src="https://www.artinsight.co.kr/data/tmp/2004/20200414154809_hzcrdnsw.jpg">
         <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">A Bigger Splash(1967)</figcaption>
      </figure>
   </div>
</div>
<div><br></div>
<div style="text-align: justify;">내가 자주 전시회를 같이 보러 다니는 사람이 세 명 있다. 그 중 두 명이나 데이비드 호크니를 최애 예술가라고 손꼽았다. 친구가 매료되었던 전시는 아시아 최초 대규모 개인전이었으며, 그 때 호크니는 국내 전시계에 첫 발을 들였다. 1년 사이에 열성적인 팬들이 몰려들었다는 것은 '도대체 그의 작품이 어떻길래?'라는 궁금증을 들게 할 수밖에 없었다.</div>
<div><br></div>
<div style="text-align: justify;">그럼에도 나는 호크니를 딱히 찾아보지는 않았다. 최근에 호크니의 신작을 보게 됐고, 고정화된 화풍이 없다는 말을 흘려들었던 것을 기억해냈다. 호크니는 진짜였다.</div>
<div><br></div>
<blockquote style="padding: 5px 10px; border: 1px solid rgb(222, 223, 223); border-image: none; background-color: #f7f7f7;">
   <p>&nbsp;</p>
   <p>I began drawing the winter trees on a new iPad, then this virus started</p>
   <p>나는 나의 새 아이패드로 겨울 나무들을 그리기 시작했고, 바이러스(코로나)가 퍼졌다.</p>
   <p style="text-align: right;">- 데이비드 호크니</p>
   <p>&nbsp;</p>
</blockquote>
<div>&nbsp;</div>
<div style="text-align: justify;">호크니는 노르망디에서 COVID-19에 대비한 자가격리 중이다. 호크니는 이 노르망디에서 3월부터 작업중이다. 현재까지 10여개의 작품을 공개했는데 정원에 앉아 아이패드로, 피어나는 봄을 그리고 있다.</div>
<div>&nbsp;</div>
<div><b><span style="font-size: 20px;">세상의 한 부분, 봄의 회복</span></b></div>
<div><b><i><span style="font-size: 16px;">the renewal that is the spring in this part of the world</span></i></b></div>
<hr style="border: medium; border-image: none; height: 1px; background-color: #999999;">
<div style="text-align: justify;">제일 먼저 그리기 시작한 것은 겨울나무이다. 우리가 서 있는 시점이 이 곳이 겨울나무가 결국 꽃을 피우는 봄이며, 현재 호크니가 가장 중요하게 보고 있는 부분이다. 병리로 시작한 대공황 상태에 대한 위로 뿐만이 아니라, 잊었던 '초록색'과의 교감 또한 권하고 있다.</div>
<div>&nbsp;</div>
<blockquote style="padding: 5px 10px; border: 1px inset rgb(204, 204, 204); border-image: none; background-color: #f7f7f7;">
   <p>&nbsp;</p>
   <p>I went on drawing the winter trees that eventually burst into blossom. This is the stage we are right now.</p>
   <p>우리가 서 있는 바로 이 시점을 그리고 있다. 그리고 그 시점은 결국 겨울나무가 꽃피울 때이다.</p>
   <p style="text-align: right;">- 데이비드 호크니</p>
   <p>&nbsp;</p>
</blockquote>
<div><br></div>
<div><b>봄은 결국 온다는 것을 기억하라. <i>Do Remember They Can't Cancel the Spring</i>.</b></div>
<div>&nbsp;</div>
<div>
   <div class="cheditor-caption-wrapper" style="text-align: center;">
      <figure class="cheditor-caption" style="margin: 0px; border: 1px solid rgb(204, 204, 204); border-image: none; width: 660px; display: inline-block; background-color: #f0f0f0;">
         <img style="height: 495px; width: 660px;" alt="Do remember they can't cancel the spring" src="https://www.artinsight.co.kr/data/tmp/2004/20200414154956_cpivtvgp.png">
         <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">Do remember they can't cancel the spring (2020)</figcaption>
      </figure>
   </div>
</div>
<div><br></div>
<div style="text-align: justify;">아무 말 없이, 미술관의 벽 한 면에서 이 풀들을 봤다면 또 스쳐 지나갈 수도 있었을 것이다. 그러나 호크니가 바이러스에 대해 직접 언급한 말들이 내가 그림들에 주의를 기울이게 했다. 나도 위로를 받고 싶었던 세상의 한 부분이기 때문에.</div>
<div><br></div>
<div style="text-align: justify;">여전히 현대사회는 복잡하고 코로나 사태는 끝날 기미가 도무지 보이질 않는다. 여기에 호크니의 신작 소식을 전한 기자는 한 쪽 눈만 가지고 세상을 보지 말자고 덧붙였다.</div>
<div><br></div>
<div style="text-align: justify;">83세의 호크니는 자신은 죽을 것이라며 담담하게 말했다. 시작이 있으면 끝이 있다. 모든 것에 말이다.</div>
<div><br></div>
<div style="text-align: justify;">실시간 스트리밍의 시대에서 우리는 현재의, 최신의 정보를 갈구한다. 현재를 살아가는 호크니가 그렇게 멋있게 느껴졌다. 나와 같은 날짜를 보내고 있는 그가 실시간으로 보내는 위로는 가히 감동이었다.</div>
<div><br></div>
<div style="text-align: justify;">코로나사태에 제한하지 않아도 상관없다. 나는 이 시간의 호크니에게 위로 받은 기억을 가지고 있고, 또 오늘을 산다. 오늘 하루는 코로나로만 설명되지 않는다.</div>
<div><br></div>
<div>그들은 봄이 오는 것을 막을 수 없다.</div>
<div>&nbsp;</div>
<div class="article-reference">참고자료</div>
<div class="article-reference">David Hockney shares exclusive art from Normandy, as 'a respite from the news' by Will Gompertz (2020.04.01)</div>"""

EN_HTML_47268 = """<div style="text-align: justify;">The popularity of fine art among the Korean public can be roughly gauged by looking at café interiors. Last autumn, Henri Matisse (1869–1954) and David Hockney (1937– ) were frequently seen. Even someone with no interest in art who has been on a Korean café tour might have glanced at the artist's name at least once, thinking, "What painting is this that it's plastered everywhere?"</div>
<div><br></div>
<div style="text-align: justify;">A friend who went to see David Hockney's exhibition at the Seoul Museum of Art in 2019 came back thrilled, calling Hockney "a madman!" She showed me <em>A Bigger Splash</em> (1967), calling it a signature work, but at the time my interest had returned to Monet (Claude Monet, 1840–1926), so I wasn't particularly drawn to it. <em>A Bigger Splash</em> (1967), with its precise division of canvas space, and Monet, standing on the exact opposite end of stylistic convention — aren't they polar opposites?</div>
<div>&nbsp;</div>
<div>
   <div class="cheditor-caption-wrapper" style="text-align: center;">
      <figure class="cheditor-caption" style="margin: 0px; border: 1px solid rgb(204, 204, 204); border-image: none; width: 660px; display: inline-block; background-color: #f0f0f0;">
         <img style="width: 660px; height: 668px;" alt="A Bigger Splash" src="https://www.artinsight.co.kr/data/tmp/2004/20200414154809_hzcrdnsw.jpg">
         <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">A Bigger Splash (1967)</figcaption>
      </figure>
   </div>
</div>
<div><br></div>
<div style="text-align: justify;">There are three people I often go to exhibitions with. Two of them named David Hockney as their all-time favorite artist. The exhibition my friend was captivated by was the first large-scale solo show in Asia, and it was Hockney's debut in the Korean exhibition world. The fact that such a passionate fanbase gathered within a year only made me more curious: "What is it about his work?"</div>
<div><br></div>
<div style="text-align: justify;">Even so, I didn't look into Hockney much after that. Recently, I came across his new works and recalled that I had brushed off the comment about him having no fixed style. Hockney was the real deal.</div>
<div><br></div>
<blockquote style="padding: 5px 10px; border: 1px solid rgb(222, 223, 223); border-image: none; background-color: #f7f7f7;">
   <p>&nbsp;</p>
   <p>I began drawing the winter trees on a new iPad, then this virus started.</p>
   <p style="text-align: right;">- David Hockney</p>
   <p>&nbsp;</p>
</blockquote>
<div>&nbsp;</div>
<div style="text-align: justify;">Hockney is in self-isolation in Normandy as a precaution against COVID-19. He has been working there since March. He has now shared over ten works — sitting in his garden, painting the blooming spring on his iPad. Had you drawn a line between an artist and the present?</div>
<div>&nbsp;</div>
<div class="article-subheading"><b><span style="font-size: 20px;">A Part of the World — The Renewal of Spring</span></b></div>
<div><i>the renewal that is the spring in this part of the world</i></div>
<div style="text-align: justify;">The first thing he began to draw was the winter trees. The moment we are standing in — this is the spring where those winter trees finally burst into bloom, and it is what Hockney considers most important right now. He offers not only consolation for a great depression that began with a pathology, but also an invitation to reconnect with the green we had forgotten.</div>
<div>&nbsp;</div>
<blockquote style="padding: 5px 10px; border: 1px inset rgb(204, 204, 204); border-image: none; background-color: #f7f7f7;">
   <p>&nbsp;</p>
   <p>I went on drawing the winter trees that eventually burst into blossom. This is the stage we are right now.</p>
   <p>It depicts the exact moment where we are standing. And that point is ultimately when the winter trees bloom.</p>
   <p style="text-align: right;">- David Hockney</p>
   <p>&nbsp;</p>
</blockquote>
<div><br></div>
<div><b>Remember they can't cancel the spring. <em>Do Remember They Can't Cancel the Spring</em>.</b></div>
<div>&nbsp;</div>
<div>
   <div class="cheditor-caption-wrapper" style="text-align: center;">
      <figure class="cheditor-caption" style="margin: 0px; border: 1px solid rgb(204, 204, 204); border-image: none; width: 660px; display: inline-block; background-color: #f0f0f0;">
         <img style="height: 495px; width: 660px;" alt="Do remember they can't cancel the spring" src="https://www.artinsight.co.kr/data/tmp/2004/20200414154956_cpivtvgp.png">
         <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">Do remember they can't cancel the spring (2020)</figcaption>
      </figure>
   </div>
</div>
<div><br></div>
<div style="text-align: justify;">If I had encountered these grasses without any context on a gallery wall, I might have walked right past them. But it was Hockney's own words about the virus that made me pay attention to his paintings. Because I, too, was a part of a world that needed consolation.</div>
<div><br></div>
<div style="text-align: justify;">Modern society remains complex and the COVID-19 crisis shows no sign of ending. The journalist who shared news of Hockney's new works added a note: let's not view the world through only one eye.</div>
<div><br></div>
<div style="text-align: justify;">83-year-old Hockney said calmly that he will die someday. If there is a beginning, there is an end. To everything.</div>
<div><br></div>
<div style="text-align: justify;">In the age of live streaming, we crave the latest, most current information. Hockney, living in the present, seemed so genuinely cool to me. The consolation he sent in real time, sharing the same calendar as me, was nothing short of moving. More so than anything excavated from any classic.</div>
<div><br></div>
<div style="text-align: justify;">It doesn't have to be confined to the COVID crisis. I carry the memory of being consoled by Hockney during this time, and I continue living today. And today cannot be explained by COVID alone.</div>
<div><br></div>
<div>They cannot cancel the spring.</div>
<div>&nbsp;</div>
<div class="article-reference">Reference</div>
<div class="article-reference">David Hockney shares exclusive art from Normandy, as 'a respite from the news' by Will Gompertz (2020.04.01)</div>"""

# Load articles
with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    if a['id'] == '47268':
        a['body_ko'] = KO_HTML_47268
        a['body_en'] = EN_HTML_47268
        print(f"Restored 47268: ko={len(a['body_ko'])}, en={len(a['body_en'])}")

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")
