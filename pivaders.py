#import potřebných knihoven
import pygame, random, time, pygame_widgets
from pygame_widgets.slider import Slider

#inicializace knihoven
pygame.init()
pygame.font.init()
pygame.mixer.init()

#načtení prvních 10000 desetinných čísel pí do seznamu pro následnou práci s nimi
pi = []
piText = "141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027590099465764078951269468398352595709825822620522489407726719478268482601476990902640136394437455305068203496252451749399651431429809190659250937221696461515709858387410597885959772975498930161753928468138268683868942774155991855925245953959431049972524680845987273644695848653836736222626099124608051243884390451244136549762780797715691435997700129616089441694868555848406353422072225828488648158456028506016842739452267467678895252138522549954666727823986456596116354886230577456498035593634568174324112515076069479451096596094025228879710893145669136867228748940560101503308617928680920874760917824938589009714909675985261365549781893129784821682998948722658804857564014270477555132379641451523746234364542858444795265867821051141354735739523113427166102135969536231442952484937187110145765403590279934403742007310578539062198387447808478489683321445713868751943506430218453191048481005370614680674919278191197939952061419663428754440643745123718192179998391015919561814675142691239748940907186494231961567945208095146550225231603881930142093762137855956638937787083039069792077346722182562599661501421503068038447734549202605414665925201497442850732518666002132434088190710486331734649651453905796268561005508106658796998163574736384052571459102897064140110971206280439039759515677157700420337869936007230558763176359421873125147120532928191826186125867321579198414848829164470609575270695722091756711672291098169091528017350671274858322287183520935396572512108357915136988209144421006751033467110314126711136990865851639831501970165151168517143765761835155650884909989859982387345528331635507647918535893226185489632132933089857064204675259070915481416549859461637180270981994309924488957571282890592323326097299712084433573265489382391193259746366730583604142813883032038249037589852437441702913276561809377344403070746921120191302033038019762110110044929321516084244485963766983895228684783123552658213144957685726243344189303968642624341077322697802807318915441101044682325271620105265227211166039666557309254711055785376346682065310989652691862056476931257058635662018558100729360659876486117910453348850346113657686753249441668039626579787718556084552965412665408530614344431858676975145661406800700237877659134401712749470420562230538994561314071127000407854733269939081454664645880797270826683063432858785698305235808933065757406795457163775254202114955761581400250126228594130216471550979259230990796547376125517656751357517829666454779174501129961489030463994713296210734043751895735961458901938971311179042978285647503203198691514028708085990480109412147221317947647772622414254854540332157185306142288137585043063321751829798662237172159160771669254748738986654949450114654062843366393790039769265672146385306736096571209180763832716641627488880078692560290228472104031721186082041900042296617119637792133757511495950156604963186294726547364252308177036751590673502350728354056704038674351362222477158915049530984448933309634087807693259939780541934144737744184263129860809988868741326047215695162396586457302163159819319516735381297416772947867242292465436680098067692823828068996400482435403701416314965897940924323789690706977942236250822168895738379862300159377647165122893578601588161755782973523344604281512627203734314653197777416031990665541876397929334419521541341899485444734567383162499341913181480927777103863877343177207545654532207770921201905166096280490926360197598828161332316663652861932668633606273567630354477628035045077723554710585954870279081435624014517180624643626794561275318134078330336254232783944975382437205835311477119926063813346776879695970309833913077109870408591337464144282277263465947047458784778720192771528073176790770715721344473060570073349243693113835049316312840425121925651798069411352801314701304781643788518529092854520116583934196562134914341595625865865570552690496520985803385072242648293972858478316305777756068887644624824685792603953527734803048029005876075825104747091643961362676044925627420420832085661190625454337213153595845068772460290161876679524061634252257719542916299193064553779914037340432875262888963995879475729174642635745525407909145135711136941091193932519107602082520261879853188770584297259167781314969900901921169717372784768472686084900337702424291651300500516832336435038951702989392233451722013812806965011784408745196012122859937162313017114448464090389064495444006198690754851602632750529834918740786680881833851022833450850486082503930213321971551843063545500766828294930413776552793975175461395398468339363830474611996653858153842056853386218672523340283087112328278921250771262946322956398989893582116745627010218356462201349671518819097303811980049734072396103685406643193950979019069963955245300545058068550195673022921913933918568034490398205955100226353536192041994745538593810234395544959778377902374216172711172364343543947822181852862408514006660443325888569867054315470696574745855033232334210730154594051655379068662733379958511562578432298827372319898757141595781119635833005940873068121602876496286744604774649159950549737425626901049037781986835938146574126804925648798556145372347867330390468838343634655379498641927056387293174872332083760112302991136793862708943879936201629515413371424892830722012690147546684765357616477379467520049075715552781965362132392640616013635815590742202020318727760527721900556148425551879253034351398442532234157623361064250639049750086562710953591946589751413103482276930624743536325691607815478181152843667957061108615331504452127473924544945423682886061340841486377670096120715124914043027253860764823634143346235189757664521641376796903149501910857598442391986291642193994907236234646844117394032659184044378051333894525742399508296591228508555821572503107125701266830240292952522011872676756220415420516184163484756516999811614101002996078386909291603028840026910414079288621507842451670908700069928212066041837180653556725253256753286129104248776182582976515795984703562226293486003415872298053498965022629174878820273420922224533985626476691490556284250391275771028402799806636582548892648802545661017296702664076559042909945681506526530537182941270336931378517860904070866711496558343434769338578171138645587367812301458768712660348913909562009939361031029161615288138437909904231747336394804575931493140529763475748119356709110137751721008031559024853090669203767192203322909433467685142214477379393751703443661991040337511173547191855046449026365512816228824462575916333039107225383742182140883508657391771509682887478265699599574490661758344137522397096834080053559849175417381883999446974867626551658276584835884531427756879002909517028352971634456212964043523117600665101241200659755851276178583829204197484423608007193045761893234922927965019875187212726750798125547095890455635792122103334669749923563025494780249011419521238281530911407907386025152274299581807247162591668545133312394804947079119153267343028244186041426363954800044800267049624820179289647669758318327131425170296923488962766844032326092752496035799646925650493681836090032380929345958897069536534940603402166544375589004563288225054525564056448246515187547119621844396582533754388569094113031509526179378002974120766514793942590298969594699556576121865619673378623625612521632086286922210327488921865436480229678070576561514463204692790682120738837781423356282360896320806822246801224826117718589638140918390367367222088832151375560037279839400415297002878307667094447456013455641725437090697939612257142989467154357846878861444581231459357198492252847160504922124247014121478057345510500801908699603302763478708108175450119307141223390866393833952942578690507643100638351983438934159613185434754649556978103829309716465143840700707360411237359984345225161050702705623526601276484830840761183013052793205427462865403603674532865105706587488225698157936789766974220575059683440869735020141020672358502007245225632651341055924019027421624843914035998953539459094407046912091409387001264560016237428802109276457931065792295524988727584610126483699989225695968815920560010165525637567"
for i in range(len(piText)):
    pi.append(piText[i])

#určení velikosti herního okna
width = 1024
height = 576
default_size = (width, height)

#nastavení zobrazení herního okna
screen = pygame.display.set_mode(default_size)
pygame.display.set_caption("PIvaders")

#nastavení defaultních fontů, konkrétně jednoho fontu různých velikostí
defFont = pygame.font.Font("media\\sfont.ttf", 30)
defFontSmall = pygame.Font("media\\sfont.ttf", 20)
defFontBig = pygame.Font("media\\sfont.ttf", 50)

#vytvoření obdélníků pro tlačítko přerušení a pro pozadí pro čísla aby nezanikaly v pozadí
pauseBut = pygame.Rect(20, 20, 25, 25)
pauseSq = pygame.Rect(25, 25, 15, 15)
digSq = pygame.Rect(42, height-52, 80, 40)
digSqw = pygame.Rect(40, height-54, 84, 44)

#import obrázků pro pozadí ze složky do programu
bgStart = pygame.image.load("media\\start.png")
bgStars = pygame.image.load("media\\stars.png")
bgEnd =  pygame.image.load("media\\end.png")

#import obrázků vršku a spodku rakety a výbuchu
top = pygame.transform.scale(pygame.image.load("media\\etop.png").convert_alpha(), (140,60))
bot = pygame.transform.scale(pygame.image.load("media\\ebot.png").convert_alpha(), (220,122))
bumImg =  pygame.image.load("media\\explosion.png").convert_alpha()

#import stažených zvuků pro zvukové efekty
pipSound = pygame.mixer.Sound("media\\pip.wav")
bumSound = pygame.mixer.Sound("media\\explode.wav")
tudumSound = pygame.mixer.Sound("media\\success.wav")
diedSound = pygame.mixer.Sound("media\\died.wav")

#upravení hlasitosti jednotlivých zvuků 
pipSound.set_volume(0.2)
diedSound.set_volume(0.6)

#přednastavení seznamu všech raket
children = []

#přednastavení 4 čísel pro ničení raket
written = ["0","0","0","0"]

#přednastavení počtu čísel pí pro rakety
nowRange = 100

#funkce pro změnu šířky obdélníčku pro skóre aby přibližně odpovídala šířce textu
def ChangeScoreWidth(score):
    return 16 + 18*(len(list(str(score))))

#funkce pro nalezení náhodného y, tak aby bylo alespoň o 40 jiné než to předchozí (vstupní parametr), aby rakety nelítali přímo za sebou
def RandY(notY, i):
        #pro náhodné y z lehce oříznuté výšky okna se následně kontroluje zda je dostatečně daleko 
        randInt = random.randint(50, height - 100)
        if i > 100 or abs(randInt - notY) > 40:
            return randInt
        #pokud není, spustí se funkce znovu pro nalezení lepšího čísla
        else: 
            return RandY(notY, i+1)
        #pokud by se stalo, že by se 100x nepovedlo najít číslo, které není v daném okolí výšky předchozí rakety, použije se jakékoli náhodné číslo


#třída rakety
class Inc:
    #inicializační funkce, přijímá parametry jaký text má nést, jaký je potřeba na její zničení a poblíž jaké výšky se nemá spawnovat
    def __init__(self, thisText, nextText, noty):
        #vždy je raketa nejdříve úplně vpravo
        self.x = width + 50
        #raketa by měla mít náhodnou výšku a zároveň neletět přímo za předchozí raketou
        self.y = RandY(noty, 1)
        #nastavení textu jako parametry objektu
        self.text = str(thisText)
        self.next = str(nextText)
        #nastavení textu, který raketa nese
        self.toWrite = defFont.render(str(thisText), True, (0,255,0))

    #funkce pro pohyb rakety
    def ChangeX(self, speed):
        #její pozice x se mění v závislosti na rychlosti hry 
        self.x -= speed


#třída pozadí
class Bg:
    #inicializace kde x je x souřadnice, kterou funkce přijímá jako parametr
    def __init__(self,x):
        self.x = x 
        #obrázkem jsou hvězdy 
        self.img = bgStars
    
    #funkce pro posun pozadí, podobně jako u rakety
    def ChangeX(self):
        self.x -= -0.1
        #pokud pozadí projede celé okno a už není vidět, přesune se opět před něj a tak se tedy mohou navzájem střídat pouze 2 různá pozadí
        if 0 < self.x - width < 0.1:
                self.x = -width


#funkce pro přílet nové rakety, parametry jsou z kolika prvních čísel pí může raketa být, kolik čísel má nést a opět jaké y vynechat
def NewInc(nowRange, digits, noy):
    #najde náhodné číslo a vytvoří raketu z daných číslic tak aby se vše vešlo do zadaného rozsahu
    randInt = random.randint(0,max(nowRange-(digits+4),0))
    first, second = "".join(pi[randInt:randInt+digits]), "".join(pi[randInt+digits:randInt+digits+4])
    theNew = Inc(first, second, noy)
    #vrátí novou raketu jako objekt a její výšku zase pro práci s výškou další rakety
    return theNew, theNew.y

#funkce pro uživatelovo selhání, parametrem je finální skore
def Died(score):
    #zahraje se zvuk prohry
    diedSound.play()
    #ukáže se pobledlejší pozadí pro dobrou čitelnost textu
    screen.fill("black")
    screen.blit(bgEnd, (0,0))
    #nastavení textu, že uživatel prohrál a jeho finální skóre
    diedTxt = defFontBig.render("You died", True, (255,255,255))
    diedTxt2 = defFontBig.render(f"Your score was {score}", True, (255,255,255))
    #následné zobrazení textu
    screen.blit(diedTxt, (width/2-90, height/2-70))
    screen.blit(diedTxt2, (width/2-190, height/2))
    pygame.display.update()

#funkce pro průběh celého gameplaye, parametry jsou podle nastavení v menu a opět zakázané y
def Run(nowRange, speed, digits, disabledY):
    #přednastavení času, skóre, proměnné pro spouštění funkce, zakázeného y, šířky skóre
    myTimer = 1.8
    timeStart = time.time()    
    score = 0
    running = True
    hissy = disabledY
    scoreWidth = 35
    
    #vytvoření 2 pozadí vedle sebe aby se mohly posouvat
    bg1, bg2 = Bg(0), Bg(-width)

    #seznam s výbuchy
    bums = []
    
    #temto loop běží dokud běží hra, tedy dokud neklikne uživatel na křížek, stop a nebo nezemře
    while running:
        #nastavení momentálního času a odečtení od časovače
        timeEnd = time.time()
        myTimer -= timeEnd - timeStart

        #pokud je časovač záporný (vypršel čas), pak přiletí nová raketa a nastaví se nový čas podle rychlosti hry
        if myTimer < 0:
            myTimer = 0.3/(speed*1.5)
            theLastOne, hissy = NewInc(nowRange, digits, hissy)
            #nová raketa se přidá do seznamu raket
            children.append(theLastOne)

        #nové nastravení času
        timeStart = time.time()

        #update obrazu
        pygame.display.update()

        #nastavení pozadí a jeho posouvání pro oba dva obrázky
        screen.fill((0,0,0))
        for bg in [bg1, bg2]:
            #zobrazení obrázku
            screen.blit(bg.img, (bg.x,0))
            #posunutí obrázku
            bg.ChangeX()

        #průběžné zrychlování hry vždy po uplynutí nějakého času
        rnTime = pygame.time.get_ticks()
        if speed < 0.1 and rnTime%2500 == 53:
            speed += 0.0005

        #nastavení obdélníčku pod skórem v závislosti na skóre
        scoreSqw = pygame.Rect(width-112, height-54, scoreWidth+4, 44)
        scoreSq = pygame.Rect(width-110, height-52, scoreWidth, 40)

        #zobrazení obdélníčků pod psanými čísly a skórem
        pygame.draw.rect(screen, (255,255,255),digSqw)
        pygame.draw.rect(screen, (255,255,255),scoreSqw)
        pygame.draw.rect(screen, (0,0,0),scoreSq)
        pygame.draw.rect(screen, (0,0,0),digSq)
        
        #nastavení a zobrazení napsaných čísel a skóre
        textWritten = "".join(written)
        destroyer = defFont.render(textWritten, True, (255,0,0))
        screen.blit(destroyer, (50, height-50))
        scoreTxt = defFont.render(str(score), True, (0,0,255))
        screen.blit(scoreTxt, (width-100, height-50))

        #zobrazení tlačítka k přerušení hry
        pygame.draw.rect(screen, (255,255,255),pauseBut)
        pygame.draw.rect(screen, (0,0,0),pauseSq)

        #loop pro všechny probíhající eventy
        for event in pygame.event.get():
            #při zmáčknutí křížku se hra přeruší změněním proměnné running a uživatel se vrátí do menu
            if event.type == pygame.QUIT:
                running = False 
            #když uživatel klikne kdekoli na pozici obdélníku přerušení tak je hra opět přerušena zpátky do menu  
            if event.type == pygame.MOUSEBUTTONUP:
                if 20 <= pygame.mouse.get_pos()[0] <= 45 and 20 <= pygame.mouse.get_pos()[1] <= 45:
                    running = False
            #pro všechny zmáčknutí kláves
            if event.type == pygame.KEYDOWN:
                #zahraje zvuk zmáčknutí
                pipSound.play()
                #pro jednotlivá čísla na numpadu nebo na hlavní klávesnici se zmáčknuté číslo připíše k napaným číslům
                #zároveň se odstraní nejstarší napsané číslo tak, aby byli vždy čísla právě 4
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    written.append("0")
                    written.pop(0)
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    written.append("1")
                    written.pop(0)
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    written.append("2")
                    written.pop(0)
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    written.append("3")
                    written.pop(0)
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    written.append("4")
                    written.pop(0)
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    written.append("5")
                    written.pop(0)
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    written.append("6")
                    written.pop(0)
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    written.append("7")
                    written.pop(0)
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    written.append("8")
                    written.pop(0)
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    written.append("9")
                    written.pop(0)
        
        #pro všechny výbuchy ze seznamu kde každý má 3 parametry: pozici x, pozici y, čas kdy vybuchnul
        for bum in bums:
            #pokud vybuchnul před méně než 0.5 sekundy, zobrazí se na obrazovce na daných souřadnicích 
            if time.time() - bum[2] < 0.5:
                screen.blit(bumImg, (bum[0]-20, bum[1]-50))
            #v opačném případě výbuch už ustal a je odebrán ze seznamu výbuchů
            else:
                bums.remove(bum)

        #pro všechny rakety na obrazovce
        for child in children:
            #pokud napsaný text odpovídá textu pro zničení rakety, raketa je odebrána ze seznamu
            if child.next == textWritten:
                children.remove(child)
                #na jejím místě se objeví výbuch
                bums.append([child.x-50, child.y-17, time.time()])
                #uživatel získá další skóre a případně se změní šířka rámečku pro skóre
                score += 1
                scoreWidth = ChangeScoreWidth(score)
                #zahraje zvuk výbuchu
                bumSound.play()
            
            #zobrazí se vršek a spodek rakety
            screen.blit(top, (child.x-50, child.y-17))
            screen.blit(bot, (child.x + (digits-6)*16, child.y-47))
            #zobrazí se text v raketě
            screen.blit(child.toWrite, (child.x,child.y-5))
            #změní se pozice x rakety v závislosti na rychlosti hry
            child.ChangeX(speed)
            #pokud raketa dolétne na konec, uživatel prohrává
            if child.x <= 0:
                timeS = time.time()
                #zobrazí se okno uživatelovi prohry
                Died(score)
                #po 2.5 sekundách se hra přeruší a uživatel je tedy zpět v menu
                while True: 
                    if time.time() - timeS > 2.5:
                        break
                running = False        
                break

        #updates the full screen
        pygame.display.flip()


#funkce při zapnutí hry pro zobrazení menu
def Test():
    #nastavení defaultní rychlosti, range, počtu číslic v raketě a proměnné pro běh menu
    speed = 0.02
    newRange = ["1","0","0"]
    running = True
    digits = 6

    #nastavení obdélníků pro tlačítko start
    myrect = pygame.Rect(width/2-150, height/2, 300, 100)
    myrectBlack = pygame.Rect(width/2-146, height/2+4, 292, 92)
    
    #nastavení hodnot, barvy a pozice sliderů
    sliderSpeed = Slider(screen, width-150, height-148, 20, 100, min=0.005, max=0.035, step=0.005, vertical = True, valueColour = "white", handleColour = (0,0,255))
    sliderDigits = Slider(screen, 50, height-148, 20, 100, min=6, max=10, step=1, initial = 6, vertical = True, valueColour = "white", handleColour = (0,0,255))

    #funkce pro běh menu
    while running:
        #zobrazení pozadí
        screen.fill("black")
        screen.blit(bgStart, (0,0))
        #zobrazení obdélníků u START
        pygame.draw.rect(screen, (255,0,0),myrect)
        pygame.draw.rect(screen, (0,0,0),myrectBlack)
        #zobrazení textu START
        startTxt = defFontBig.render("START", True, (255,255,255))
        screen.blit(startTxt, (width/2-70, height/2+20))

        #nastavení a zobrazení textu pro zadání počtu číslic pí
        rangeTxt = defFont.render(str("".join(newRange)), True, (255,255,255))
        screen.blit(rangeTxt, (370, height-80))
        yourRangeTxt = defFontSmall.render("Input range (max 4 digits)", True, "white") # minimum je však 10, maximum 9999
        screen.blit(yourRangeTxt, (370, height-110))

        #nastavení a zobrazení hodnot u slideru s nastavením rychlosti hry
        fastTxt = defFontSmall.render("fast", True, "white") 
        screen.blit(fastTxt, (width-115, height-160))
        defaultTxt = defFontSmall.render("default", True, "white") 
        screen.blit(defaultTxt, (width-115, height-110))
        slowTxt = defFontSmall.render("slow", True, "white") 
        screen.blit(slowTxt, (width-115, height-60))

        #nastavení a zobrazení hodnout u slideru s nastavením počtu číslic v raketě (od 6 do 10)
        sixTxt = defFontSmall.render("6", True, "white") 
        screen.blit(sixTxt, (85, height-60))
        sevenTxt = defFontSmall.render("7", True, "white") 
        screen.blit(sevenTxt, (85, height-85))
        eightTxt = defFontSmall.render("8", True, "white") 
        screen.blit(eightTxt, (85, height-110))
        nineTxt = defFontSmall.render("9", True, "white") 
        screen.blit(nineTxt, (85, height-135))
        tenTxt = defFontSmall.render("10", True, "white") 
        screen.blit(tenTxt, (85, height-160))

        #nastavení a zobrazení názvů pro slidery
        digitsTxt = defFontSmall.render("digits as a hint", True, "white") 
        screen.blit(digitsTxt, (50, height-195))
        speedTxt = defFontSmall.render("speed", True, "white") 
        screen.blit(speedTxt, (width-150, height-200))

        #uložení hodnot ze sliderů do proměnných
        events = pygame.event.get()
        speed = sliderSpeed.getValue()
        digits = sliderDigits.getValue()

        #aktualizace zobrazení sliderů
        pygame_widgets.update(events)

        #loop procházející všechny eventy
        for event in events:
            #při zmáčknutí křížku je hra ukončena
            if event.type == pygame.QUIT:
                running = False 
            #pokud je myší kliknuto kdekoli na obdélníku značícím tlačítko start, spustí se hra
            if event.type == pygame.MOUSEBUTTONUP:
                if width/2-150 <= pygame.mouse.get_pos()[0] <= width/2+150 and height/2 <= pygame.mouse.get_pos()[1] <= height/2+100:
                    #seznam všech raket je vyprázdněn
                    for _ in range(len(children)):
                        children.pop()
                    
                    #rovnou je nastavena první raketa s prvními n číslicemi pí na náhodné výšce a je přidána do seznamu, všechny ostatní už mají čísla náhodně
                    firstBorn = Inc("".join(pi[0:digits]), "".join(pi[digits:digits+4]), 0) 
                    children.append(firstBorn)
                    
                    #napsané číslice jsou resetovány
                    for _ in range(4):
                        written.append("0")
                        written.pop(0)
                    
                    #je nastaven range čísel pí
                    nowRange = int("".join(newRange))
                    #zahraje zvuk pro start hry
                    tudumSound.play()
                    #spustí se funkce pro běh hry
                    Run(nowRange, speed, digits, firstBorn.y)

            #pokud je zmáčknutá klávesa na klávesnici, zahraje se zvuk
            if event.type == pygame.KEYDOWN:
                pipSound.play()
                #pro všechny čísla se zmáčknuté číslo připíše k rozsahu čísel pí
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    newRange.append("0")
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    newRange.append("1")
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    newRange.append("2")
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    newRange.append("3")
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    newRange.append("4")
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    newRange.append("5")
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    newRange.append("6")
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    newRange.append("7")
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    newRange.append("8")
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    newRange.append("9")

                #pokud je na začátku 0 a je za ní jiné číslo, nula se smaže
                if len(newRange) != 0 and newRange[0] == "0" and len(newRange) >= 2:
                    newRange.pop(0)

                #pokud by měl být seznam delší než 5, smaže se poslední číslo (tedy právě napsané)
                #maximum je tedy 9999 číslic
                if len(newRange) >= 5:
                    newRange.pop()

                #při zmáčknutí backspace se odstraní poslední číslo
                if len(newRange) != 0 and event.key == pygame.K_BACKSPACE:
                    newRange.pop()

        #aktualizace zobrazení 
        pygame.display.update()
        pygame.display.flip()

#spuštění menu při startu hry
Test()

#při ukončení všech funkcí zavření okna
pygame.quit()