import json
import re

KO_HTML_51061 = """<p style="text-align: justify; "><b>&nbsp;</b></p>
<p style="text-align: justify; "><b>&nbsp;</b></p>
<p style="text-align: justify; "><b><span style="font-size: 20px;">나의 스마트폰 중독기</span></b></p>
<hr style="height: 1px; background-color: #999999; border: none;">
<p>&nbsp;</p>
<p style="text-align: justify; ">스마트폰 중독이 별건가. 고3 수험생 시절엔 집에 핸드폰을 두고 다녔었는데 그닥 힘들지 않았다. 그때처럼 거리를 두면 금방 고쳐질 것 아닌가.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">하지만 그 때의 것과 지금의 것은 달랐다. 단 몇 주만에도 업데이트를 해야하는 스마트폰이 연 단위로는 가늠할 수 없을만큼 진화하는데도 나는 여전히 같은 크기의 영향력을 가졌을 것이라고 여겼다. 이 기기와 스스로의 제어능력에 대한 자만과 오만함이 동시에 발현된 것이다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">그럴 만한 것이 내가 기억하는 최초의 소셜 미디어는 버디버디였고, 계정조차 없었다. 그 이후의 SNS 역시도 거의 사용하지 않았다. 그러다가 배낭여행을 하게 됐고, 핸드폰 도난에 대비해 사진을 틈틈히 업로드 해놓는 것이 좋다는 조언에 인스타그램에 본격적으로 몰입하게 되었다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">인스타그램이 열어놓은 시대는 조금 달랐다. 남미여행의 사진에 태그 한마디만 걸어 놓았을 뿐인데 이벤트에 당첨이 되었고, 여행 사진들로 적지않은 팔로워가 모여 대외활동 여럿에 활동할 수 있었다. 사진 한 장으로 식당에서는 음료수와 같은 서비스를 받을 수 있고, 청계천을 걷다가 발견한 이벤트 부스에서는 계정만 팔로우하면 꽤 가격이 나가는 브랜드의 클러치를 증정해 주었다. 인스타그램을 하지 않는다는 것은 모두가 갖는 기회를 외면하는 것이었다. 굳이 그럴 이유가 없다. 나만 혜택을 누리지 못할 이유가.</p>
<p style="text-align: justify;">&nbsp;</p>
<div class="cheditor-caption-wrapper" style="text-align: center;">
   <figure class="cheditor-caption" style="border: 1px solid rgb(204, 204, 204); background-color: #f0f0f0; margin: 0px; display: inline-block; width: 660px;"><img src="https://www.artinsight.co.kr/data/tmp/2012/20201201050507_tbqwrzhm.jpg" alt="iStock_81484743_MEDIUM.jpg" style="width: 660px; height: 293px;">
      <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">istockphoto</figcaption>
      </figure>
   </div>
<p>&nbsp;</p>
<p style="text-align: justify;">얼마전에는 게임이 로딩되는 그 짧은 시간마다 소셜 미디어를 확인하는 나를 발견했다. 카카오톡이나 인스타그램보다도 지역 소셜 당근마켓, 대학원 커뮤니티나 주식정보 커뮤니티가 있는 카카오톡 오픈채팅, 또 덕질을 위한 트위터, 학업 정보가 업데이트되는 네이버 카페, 대외활동이나 취미생활을 작성하는 네이버 블로그까지(아직 끝나지 않았지만 이만 줄이도록 하겠다). 확인해야할 것들이 너무 많았기 때문이다. 게임을 하는 도중에는 알고리즘에 따라 유튜브를 틀어놓기까지 했더라.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">일반적으로 생각하는 SNS인 카카오톡 메신저, 인스타그램의 응답 속도가 느리다는 이유로 나는 스마트폰 중독과는 거리가 멀 것이라고 생각했다. 그치만 나 역시 중독자였던 거다. 한국정보화진흥원은 스마트폰 중독을 게임중독, 콘텐츠중독, SNS중독, 정보중독 등으로 분류한다. 이 중에서 나의 SNS 생활만 관찰해봤는데도 걷잡을 수가 없었다.</p>
<p style="text-align: justify;"><br></p>
<p style="text-align: justify;"><b><span style="font-size: 20px;">나를 중독시키는 단 하나의 스마트 기기</span></b></p>
<hr style="height: 1px; background-color: #999999; border: none;">
<p>&nbsp;</p>
<p style="text-align: justify;">재택근무가 증가하는 추세인 지금, 휴식이 휴식이 아닌 것처럼 느껴지고, 일을 하는 것도 안하는 것도 아닌 것처럼 느껴지는 이유가 한 공간에서 다수의 작업을 하고 있기 때문이다. 각 장소가 한정된 역할을 하는 것이 아니기 때문에 개인 내면에서 추상적으로 분리해야 하는데, 생각보다 쉽지가 않다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">따라서 집이 아닌 방에 거주하는 n룸세대에게 가장 중요한 인테리어 원칙은 공간의 '분리'이다. 파티션과 가벽, 커튼, 책장을 요리조리 배치하여 취침, 공부, 요리 등 작업 별로 경계선을 마련하면 시각적으로 확인이 가능해 심리적 준비를 용이하게 할 수 있다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">그러나 디지털 기기의 필드에서는 정반대의 상황이 벌어지고 있다. 카메라, 필기구, 책, 게임, 쇼핑, 학습 또는 오피스 작업 등이 한 데 모여 태블릿 pc까지 왔다(너무 많아서 AI비서까지 말하기도 힘들다). 생활 전반을 담당하며 혁신이라 불리는 A4 종이 크기의 작은 괴물은 모든 것의 경계를 무너뜨렸다. 좋게 말하면 멀티태스킹이고, 나쁘게 말하면 짬뽕인거다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">현대의 기술은 하나의 콤팩트한 직사각형으로 응집되었지만, 이동성이 간편해진만큼 물리적 분리의 장점을 놓쳤다. 잠들기 직전까지, 막 일어난 후까지 점령한 과학기술을 일상생활에서 다시 떼어낼 필요가 있어 보인다. 세계화와 지역화가 동시에 진행되는 것처럼, 집합체 내에서 개별성을 골라내는 새로운 방법이 필요하다. 언제금 다시 태블릿을 여러개의 기기로 분할 구입하게 되어도 기꺼이 값을 지불할 사람들이 많아질 수 있다.</p>
<p style="text-align: justify;">&nbsp;</p>
<div class="cheditor-caption-wrapper" style="text-align: center;">
   <figure class="cheditor-caption" style="border: 1px solid rgb(204, 204, 204); background-color: #f0f0f0; margin: 0px; display: inline-block; width: 600px;"><img src="https://www.artinsight.co.kr/data/tmp/2012/20201201050845_xxsaeufb.jpg" alt="techrepublic.jpg" style="width: 600px; height: 400px;">
      <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">istockphoto</figcaption>
      </figure>
   </div>
<p>&nbsp;</p>
<p style="text-align: justify;">다큐멘터리 &lt;소셜딜레마(2020)&gt;에 따르면 최근 젊은 세대는 운전면허증 취득률까지 현저히 하락했을 정도로 현실세계를 배제한 채 디지털세계에 몰입했다. 이 세대의 특징은 디지털 자아(Digital Self)를 따로 생성하는 데에 있다. 문제는 디지털 자아에 현실 자아보다 더 많은 시간을 투자한다는 것이며, 이 두가지의 자아를 전혀 분리하지 못한다는 것이다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">대면 커뮤니케이션보다 필터링 기능이 약한 디지털 커뮤니케이션에서 받은 타격은 그대로 현실 자아에까지 영향을 미쳐, 갈수록 불안하고 우울한 사회가 되어간다. 실재의 본인은 한 사람에 국한되나, 감당되지 않는 개수의 자아를 따로 생성한 까닭에 컨트롤타워에 한계가 왔다.</p>
<p style="text-align: justify;"><br></p>
<blockquote style="border: 1px inset rgb(204, 204, 204); background-color: #d97706; padding: 5px 10px;">
   <p>&nbsp;</p>
   <p>"This is checkmate on humanity."</p>
   <p style="text-align: justify; ">"이건 인간사회에 날리는 마지막 경고입니다."</p>
   <p style="text-align: right;"><b>&nbsp;</b></p>
   <p style="text-align: right;">- 소셜딜레마, The Social Dilemma (2020)</p>
   <p style="text-align: center;"><b>&nbsp;</b></p>
   </blockquote>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: justify;">현재 수많은 지표들이 현대 인간에게 경고하고 있다. 그러나 다수의 사람들이 자각하는 디지털 시대의 취약점에 대해 논의하는 장이 열린 것을 체크메이트라고 해석하고 싶다. 이 대화가 묵살된다면 게임이 끝나는 것.</p>
<p style="text-align: justify;">&nbsp;</p>
<blockquote style="border: 1px inset rgb(204, 204, 204); background-color: #d97706; padding: 5px 10px;">
   <p>&nbsp;</p>
   <p>"Think we're gonna get there? 우리가 해결할 수 있을까요?"</p>
   <p style="text-align: justify; ">"We have to. 그래야만 하죠."</p>
   <p><b>&nbsp;</b></p>
   <p style="text-align: right; ">- 소셜딜레마, The Social Dilemma (2020)</p>
   <p>&nbsp;</p>
   </blockquote>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">넷플릭스 오리지널 다큐멘터리 &lt;소셜딜레마(2020)&gt;을 태블릿을 이용해 보고 통탄하는 나. &lt;소셜딜레마&gt;에 대한 다른 이들의 의견을 영화 평점 소셜 어플인 왓챠피디아에서 확인하는 나. 이 글을 쓰는 작업까지도 디지털 기기를 이용하고 있는 나. 이것이 딜레마고, 누구나 느끼고 있는 점이다.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">현재를 내다 버릴 필요는 없다. 현재를 전부 부정할 필요는 없다. 인간은 더 나은 길을 찾을 수 있고, 찾아야 하는 국면에 다달았다. 그 길의 기반은 현재까지의 기술력이 밑받침 될 것이다. 동일 기술이라고 하더라도 활용 양상에 따라 결과는 확연히 변할 것이고, 발전 방향을 수립할 수 있을 것이다. 디지털 프랑켄슈타인이라고도 명명하는 현대인이 기술에 잠식되지 않기 위해서는 분리의 해법을 더 고심해야 한다.</p>"""

EN_HTML_51061 = """<p class="article-subheading" style="text-align: justify; "><b><span style="font-size: 20px;">My Smartphone Addiction</span></b></p>
<p style="text-align: justify; ">Is smartphone addiction a big deal? Back when I was studying for my college entrance exams in high school, I would leave my phone at home and it wasn't that hard. Wouldn't keeping that kind of distance again fix it quickly?</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">But the situation then and now were different. Even as smartphones that require updates every few weeks have evolved to an unimaginable degree year after year, I still assumed I had the same level of control over them. It was a simultaneous expression of arrogance and hubris — both toward the device and toward my own self-control.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">For context, the first social media I can remember is Buddy Buddy, and I didn't even have an account. I barely used SNS after that either. Then I went backpacking, and on someone's advice to upload photos regularly in case my phone got stolen, I dove headfirst into Instagram.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">The era Instagram opened up was a little different. I only added a single tag to a photo from my South America trip, and I won an event. With my travel photos, a decent following gathered and I was able to participate in several external activities. With just one photo, I could receive drinks at a restaurant, and at an event booth I found walking along Cheonggyecheon, you only needed to follow an account to receive a clutch from a fairly pricey brand. Not being on Instagram meant ignoring opportunities that everyone else had. There was no reason to do that. No reason why only I shouldn't enjoy the benefits.</p>
<p style="text-align: justify;">&nbsp;</p>
<div class="cheditor-caption-wrapper" style="text-align: center;">
   <figure class="cheditor-caption" style="border: 1px solid rgb(204, 204, 204); background-color: #f0f0f0; margin: 0px; display: inline-block; width: 660px;"><img src="https://www.artinsight.co.kr/data/tmp/2012/20201201050507_tbqwrzhm.jpg" alt="iStock_81484743_MEDIUM.jpg" style="width: 660px; height: 293px;">
      <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">istockphoto</figcaption>
      </figure>
   </div>
<p style="text-align: justify;">Not long ago, I caught myself checking social media during every short loading screen while gaming. Not just KakaoTalk or Instagram — but Karrot Market for local community, KakaoTalk Open Chats for grad school and stock info communities, Twitter for fandom stuff, Naver Cafes for academic updates, and Naver Blog for extracurricular activities and hobbies (I could keep going, but I'll stop here). There were simply too many things to check. I even had YouTube on in the background while gaming, following the algorithm.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">Because I'm slow to respond to KakaoTalk and Instagram — the SNS most people think of — I assumed I was far from smartphone addiction. But I was an addict too. The Korea Information Society Development Institute categorizes smartphone addiction into game addiction, content addiction, SNS addiction, and information addiction. Even just observing my own SNS life among those categories, it was out of control.</p>
<p style="text-align: justify;"><br></p>
<p class="article-subheading" style="text-align: justify; "><b><span style="font-size: 20px;">The One Smart Device That Addicts Me</span></b></p>
<p style="text-align: justify;">With remote work on the rise, the reason rest doesn't feel like rest, and work doesn't feel like work or not-work, is that we're doing multiple things in a single space. Because each location no longer serves a limited role, we have to abstractly separate them in our minds — and that's harder than it sounds.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">For this reason, the most important interior design principle for the N-room generation living in rooms rather than full apartments is the concept of 'separation.' By creatively positioning partitions, half-walls, curtains, and bookshelves to create boundaries for sleeping, studying, cooking and other tasks, you make things visually clear, which makes psychological preparation easier.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">But in the field of digital devices, the exact opposite is happening. Cameras, writing tools, books, games, shopping, learning, and office work have all converged — we've arrived at the tablet PC (there's so much I can hardly even mention AI assistants). The small A4-paper-sized monster, responsible for all of life and called an innovation, has torn down all boundaries. Put nicely, it's multitasking. Put bluntly, it's a jumble.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">Modern technology has condensed into one compact rectangle, and while mobility has become easier, the advantages of physical separation have been lost. It seems we need to find ways to detach from the technology that occupies us right up until we fall asleep and the moment we wake up. Just as globalization and localization proceed simultaneously, we need new ways to extract individuality from within the collective. There may come a day when many people are willing to pay to split the tablet back into multiple separate devices.</p>
<p style="text-align: justify;">&nbsp;</p>
<div class="cheditor-caption-wrapper" style="text-align: center;">
   <figure class="cheditor-caption" style="border: 1px solid rgb(204, 204, 204); background-color: #f0f0f0; margin: 0px; display: inline-block; width: 600px;"><img src="https://www.artinsight.co.kr/data/tmp/2012/20201201050845_xxsaeufb.jpg" alt="techrepublic.jpg" style="width: 600px; height: 400px;">
      <figcaption class="cheditor-caption-text" style="margin: 6px 10px 6px 10px; text-align: left; line-height: 18px; font-size: 12px; letter-spacing: -0.04em; text-align:justify;">istockphoto</figcaption>
      </figure>
   </div>
<p style="text-align: justify;">According to the Netflix documentary <em>The Social Dilemma</em> (2020), recent younger generations have become so immersed in the digital world — to the exclusion of the real one — that even driver's license acquisition rates have dropped significantly. A defining characteristic of this generation is that they create a separate Digital Self. The problem is that they invest more time in that digital self than in their real self, and they cannot separate the two at all.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">The blows received through digital communication, which has weaker filtering mechanisms than face-to-face communication, directly impact the real self — creating an increasingly anxious and depressed society. The real person is just one individual, yet they have created an unmanageable number of selves, and the control center has reached its limits.</p>
<p style="text-align: justify;"><br></p>
<blockquote style="border: 1px inset rgb(204, 204, 204); background-color: #d97706; padding: 5px 10px;">
   <p>&nbsp;</p>
   <p>"This is checkmate on humanity."</p>
   <p style="text-align: justify; ">"This is the final warning to human society."</p>
   <p style="text-align: right;"><b>&nbsp;</b></p>
   <p style="text-align: right;">- The Social Dilemma (2020)</p>
   <p style="text-align: center;"><b>&nbsp;</b></p>
   </blockquote>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: justify;">Countless indicators are currently warning modern humans. But I'd like to interpret the opening of a dialogue — where many people are aware of and discussing the vulnerabilities of the digital age — as checkmate itself. If this conversation is silenced, the game ends.</p>
<p style="text-align: justify;">&nbsp;</p>
<blockquote style="border: 1px inset rgb(204, 204, 204); background-color: #d97706; padding: 5px 10px;">
   <p>&nbsp;</p>
   <p>"Think we're gonna get there?"</p>
   <p style="text-align: justify; ">"We have to."</p>
   <p><b>&nbsp;</b></p>
   <p style="text-align: right; ">- The Social Dilemma (2020)</p>
   <p>&nbsp;</p>
   </blockquote>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">Me, watching the Netflix original documentary <em>The Social Dilemma</em> (2020) on a tablet and lamenting. Me, checking other people's opinions on the film on Watcha Pedia, a social film rating app. Me, even writing this article using a digital device. This is the dilemma, and it's something everyone feels.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;">We don't need to throw away the present. We don't need to deny everything about now. Humans can find a better path, and we've reached a juncture where we must. That path will be built on the technology we've developed thus far. Even with the same technology, results will change significantly depending on how it's used, and from there we can establish a direction for development. Modern humans — sometimes called Digital Frankensteins — must think more carefully about solutions to separation in order to avoid being consumed by technology.</p>"""

# Load articles
with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    if a['id'] == '51061':
        a['body_ko'] = KO_HTML_51061
        a['body_en'] = EN_HTML_51061
        print(f"Restored 51061: ko={len(a['body_ko'])}, en={len(a['body_en'])}")

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")
