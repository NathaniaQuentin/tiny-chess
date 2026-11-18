import json,os,sys,urllib.request,urllib.error,random
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no env")
V=[0,100,320,330,500,900,0]
ND=[-33,-31,-18,-14,14,18,31,33]
KD=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17];RD=[-16,-1,1,16]
MATE=100000
def _pst():
 P=[0]*64;N=[0]*64;B=[0]*64;R=[0]*64;Q=[0]*64;K=[0]*64;E=[0]*64
 pa=[0,0,4,8,14,24,40,0];pc=[0,0,0,10,15,10,5,0]
 for r in range(8):
  for f in range(8):
   i=r*8+f;c=min(f,7-f)+min(r,7-r)
   P[i]=pa[r]+(pc[r] if f in(3,4)else 0);N[i]=6*c-20;B[i]=4*c-8
   R[i]=(15 if r==6 else 0)+(5 if r==0 and f in(3,4)else 0);Q[i]=2*c-6
   K[i]=[20,25,10,0,0,10,25,20][f] if r==0 else max(-50,-15*r);E[i]=8*c-24
 return P,N,B,R,Q,K,E
PST=_pst()
PP=[0,0,6,14,28,48,80,0]
_r=random.Random(20261117)
Z=[[ _r.getrandbits(64) for _ in range(128)] for _ in range(12)]
ZS=_r.getrandbits(64);ZC=[_r.getrandbits(64) for _ in range(16)];ZE=[_r.getrandbits(64) for _ in range(8)]
def zi(p):return p+5 if p>0 else p+6
b=[0]*128;side=1;cast=0;ep=-1;half=0;h=0;sc=0;nm=0
wm=[0]*8;bm=[0]*8;ks=[0,0];bc=[0,0]
stk=[];rc={};tt={}
kill=[[0,0] for _ in range(64)]
nodes=0;LM=0;BG=60000
class AB(Exception):pass
def cv(p,s):
 t=p if p>0 else -p;r=s>>4;f=s&7
 i=r*8+f if p>0 else (7-r)*8+f
 return (V[t]+PST[t-1][i])*(1 if p>0 else -1)
def atk(s,by):
 if by>0:
  if not(s-15&136)and b[s-15]==1:return 1
  if not(s-17&136)and b[s-17]==1:return 1
 else:
  if not(s+15&136)and b[s+15]==-1:return 1
  if not(s+17&136)and b[s+17]==-1:return 1
 for d in ND:
  u=s+d
  if not(u&136)and b[u]==2*by:return 1
 for d in KD:
  u=s+d
  if not(u&136)and b[u]==6*by:return 1
 for d in BD:
  u=s+d
  while not(u&136):
   q=b[u]
   if q:
    if q==3*by or q==5*by:return 1
    break
   u+=d
 for d in RD:
  u=s+d
  while not(u&136):
   q=b[u]
   if q:
    if q==4*by or q==5*by:return 1
    break
   u+=d
 return 0
def tog(c,f,r):
 if c==0:wm[f]^=1<<r
 else:bm[f]^=1<<r
def gen(caps):
 ms=[]
 for s in range(128):
  if s&136:continue
  p=b[s]
  if p==0 or(p>0)!=(side>0):continue
  t=p if p>0 else -p
  if t==1:
   d=16 if p>0 else -16;r=s>>4
   u=s+d
   if b[u]==0:
    prm=(p>0 and r==6)or(p<0 and r==1)
    if prm:
     for pr in(5,4,3,2):ms.append(s|u<<7|pr<<14)
    elif not caps:
     ms.append(s|u<<7)
     if(p>0 and r==1)or(p<0 and r==6):
      u2=s+2*d
      if b[u2]==0:ms.append(s|u2<<7)
   for dd in(d-1,d+1):
    u=s+dd
    if u&136:continue
    q=b[u]
    if q!=0 and(q>0)!=(p>0):
     if(p>0 and r==6)or(p<0 and r==1):
      for pr in(5,4,3,2):ms.append(s|u<<7|pr<<14)
     else:ms.append(s|u<<7)
    elif u==ep:ms.append(s|u<<7)
  elif t==2 or t==6:
   for dd in ND if t==2 else KD:
    u=s+dd
    if u&136:continue
    q=b[u]
    if q==0:
     if not caps:ms.append(s|u<<7)
    elif(q>0)!=(p>0):ms.append(s|u<<7)
  else:
   ds=BD if t==3 else RD if t==4 else BD+RD
   for dd in ds:
    u=s+dd
    while not(u&136):
     q=b[u]
     if q==0:
      if not caps:ms.append(s|u<<7)
     else:
      if(q>0)!=(p>0):ms.append(s|u<<7)
      break
     u+=dd
 if not caps:
  for C,K,A,Q,R,D in((1,4,5,6,7,6),(2,4,3,2,0,2),(4,116,117,118,119,118),(8,116,115,114,112,114)):
   if cast&C and b[A]==0 and b[Q]==0 and b[D-1]==0 and b[R]==(4 if K<16 else -4) and not atk(K,-side)and not atk(A,-side)and not atk(D,-side):ms.append(K|D<<7)
 return ms
def make(m):
 global side,cast,ep,half,h,sc,nm
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 pc=b[f];cap=b[t];cs=-1;rf=-1
 if abs(pc)==1 and(f&7)!=(t&7)and cap==0:
  cs=t-16 if pc>0 else t+16;cap=b[cs]
 if abs(pc)==6 and abs(t-f)==2:rf=f+3 if t>f else f-4
 stk.append((m,pc,cap,cs,rf,cast,ep,half,h,sc,nm,bc[0],bc[1],ks[0],ks[1]))
 h^=Z[zi(pc)][f];h^=ZS
 if ep>=0:h^=ZE[ep&7]
 h^=ZC[cast]
 sc-=cv(pc,f)
 np1=pr if pr else abs(pc);np=np1 if pc>0 else -np1
 sc+=cv(np,t)
 if cap:
  sc-=cv(cap,cs if cs>=0 else t)
  if abs(cap)>1:nm-=V[abs(cap)]
  if abs(cap)==3:bc[0 if cap>0 else 1]-=1
 if pr:
  nm+=V[pr]-100
  if pr==3:bc[0 if pc>0 else 1]+=1
 if abs(pc)==1:
  tog(0 if pc>0 else 1,f&7,f>>4);tog(0 if pc>0 else 1,t&7,t>>4)
  if cap:tog(0 if cap>0 else 1,(cs if cs>=0 else t)&7,(cs if cs>=0 else t)>>4)
 if abs(pc)==6:ks[0 if pc>0 else 1]=t
 if rf>=0:
  rk=4 if pc>0 else -4;rt=f+1 if t>f else f-1
  sc-=cv(rk,rf);sc+=cv(rk,rt);h^=Z[zi(rk)][rf];h^=Z[zi(rk)][rt]
  b[rf]=0;b[rt]=rk
 h^=Z[zi(np)][t]
 if cap:h^=Z[zi(cap)][cs if cs>=0 else t]
 b[f]=0;b[t]=np
 if cs>=0:b[cs]=0
 nc=cast
 if abs(pc)==6:nc&=~3 if pc>0 else ~12
 if f==0 or t==0:nc&=~2
 if f==7 or t==7:nc&=~1
 if f==112 or t==112:nc&=~8
 if f==119 or t==119:nc&=~4
 if nc!=cast:h^=ZC[nc];cast=nc
 ep=(f+t)//2 if abs(pc)==1 and abs(t-f)==32 else -1
 if ep>=0:h^=ZE[ep&7]
 half=0 if abs(pc)==1 or cap else half+1
 side=-side
 rc[h]=rc.get(h,0)+1
 if atk(ks[0] if side<0 else ks[1],side):
  unmake();return 0
 return 1
def unmake():
 global side,cast,ep,half,h,sc,nm
 m,pc,cap,cs,rf,cast0,ep0,half0,h0,sc0,nm0,bc0,bc1,k0,k1=stk.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 rc[h]-=1
 if abs(pc)==1:
  tog(0 if pc>0 else 1,f&7,f>>4);tog(0 if pc>0 else 1,t&7,t>>4)
  if cap:tog(0 if cap>0 else 1,(cs if cs>=0 else t)&7,(cs if cs>=0 else t)>>4)
 b[f]=pc;b[t]=0
 if cs>=0:b[cs]=cap
 elif cap:b[t]=cap
 if rf>=0:
  rt=f+1 if t>f else f-1
  b[rf]=4 if pc>0 else -4;b[rt]=0
 cast,ep,half,h,sc,nm=cast0,ep0,half0,h0,sc0,nm0
 bc[0],bc[1]=bc0,bc1;ks[0],ks[1]=k0,k1
 side=-side
def pstruct(c):
 m=wm if c==0 else bm;em=bm if c==0 else wm;s=0
 for f in range(8):
  w=m[f]
  while w:
   lb=w&-w;r=lb.bit_length()-1;w^=lb
   if(f==0 or not m[f-1])and(f==7 or not m[f+1]):s-=8
   e=em[f-1] if f>0 else 0;e|=em[f]
   if f<7:e|=em[f+1]
   if c==0:
    if e>>(r+1)==0:s+=PP[r]
   elif e&((1<<r)-1)==0:s+=PP[7-r]
 return s
def ev():
 s=sc
 if bc[0]>1:s+=30
 if bc[1]>1:s-=30
 ph=nm if nm<6400 else 6400
 for c in(0,1):
  k=ks[c];r=k>>4;f=k&7;i=r*8+f if c==0 else(7-r)*8+f
  kv=(PST[5][i]*ph+PST[6][i]*(6400-ph))//6400
  s+=kv if c==0 else -kv
 s+=pstruct(0)-pstruct(1)
 return s if side>0 else -s
def order(ms,ttm,ply):
 def key(m):
  if m==ttm:return 1<<20
  f=m&127;t=(m>>7)&127;pr=(m>>14)&7
  cap=b[t]
  if cap:return 10000+V[abs(cap)]*10-V[abs(b[f])]
  if pr:return 9000+V[pr]*10
  if m==kill[ply][0]:return 8000
  if m==kill[ply][1]:return 7000
  return 0
 ms.sort(key=key,reverse=True)
 return ms
def qs(a,be,ply):
 global nodes
 nodes+=1
 if LM and nodes>=LM:raise AB
 if ply>0 and(half>=100 or rc.get(h,0)>1):return 0
 chk=atk(ks[0] if side>0 else ks[1],-side)
 if not chk:
  s=ev()
  if s>=be:return s
  if s>a:a=s
  best=s
 else:best=-MATE
 legal=0
 for m in order(gen(0 if chk else 1),0,ply):
  if not make(m):continue
  legal+=1
  try:s=-qs(-be,-a,ply+1)
  except AB:unmake();raise
  unmake()
  if s>best:best=s
  if s>=be:return s
  if s>a:a=s
 if chk and legal==0:return -MATE+ply
 return best
def srch(d,a,be,ply):
 global nodes,ep,h,side
 nodes+=1
 if LM and nodes>=LM:raise AB
 if ply>0 and(half>=100 or rc.get(h,0)>1):return 0
 chk=atk(ks[0] if side>0 else ks[1],-side)
 if chk:d+=1
 if d<=0:return qs(a,be,ply)
 e=tt.get(h);ttm=0
 if e:
  if e[0]>=d:
   s=e[1]
   if s>MATE-1000:s-=ply
   elif s<-MATE+1000:s+=ply
   if e[2]==0:return s
   if e[2]==1 and s>=be:return s
   if e[2]==2 and s<=a:return s
  ttm=e[3]
 if d>=3 and not chk and nm>600:
  e0=ep;h0=h
  h^=ZS
  if ep>=0:h^=ZE[ep&7]
  ep=-1;side=-side;rc[h]=rc.get(h,0)+1
  try:s=-srch(d-3,-be,-be+1,ply+1)
  except AB:rc[h]-=1;side=-side;ep=e0;h=h0;raise
  rc[h]-=1;side=-side;ep=e0;h=h0
  if s>=be:return s
 a0=a;best=-MATE;bestm=0;legal=0
 for m in order(gen(0),ttm,ply):
  if not make(m):continue
  legal+=1
  try:s=-srch(d-1,-be,-a,ply+1)
  except AB:unmake();raise
  unmake()
  if s>best:best=s;bestm=m
  if s>a:a=s
  if a>=be:
   t=(m>>7)&127
   if b[t]==0 and not((m>>14)&7):
    if kill[ply][0]!=m:kill[ply][1]=kill[ply][0];kill[ply][0]=m
   break
 if legal==0:return -MATE+ply if chk else 0
 s=best
 if s>MATE-1000:s+=ply
 elif s<-MATE+1000:s-=ply
 tt[h]=(d,s,0 if best>a0 and best<be else 1 if best>=be else 2,bestm)
 return best
def root(legal):
 global nodes,LM
 nodes=0;best=legal[0]
 for d in range(1,13):
  LM=0 if d==1 else BG
  try:
   a=-MATE-1;bb=MATE+1;cb=best;bv=-MATE-1
   for m in legal:
    if not make(m):continue
    try:s=-srch(d-1,-bb,-a,1)
    except AB:unmake();raise
    unmake()
    if s>bv:bv=s;cb=m
    if s>a:a=s
   best=cb;legal.remove(cb);legal.insert(0,cb)
  except AB:break
 return best
def scan():
 global h,sc,nm
 h=ZS if side<0 else 0;sc=0;nm=0
 for i in range(8):wm[i]=0;bm[i]=0
 bc[0]=0;bc[1]=0
 for s in range(128):
  if s&136:continue
  p=b[s]
  if not p:continue
  h^=Z[zi(p)][s];sc+=cv(p,s)
  t=p if p>0 else -p
  if t==6:ks[0 if p>0 else 1]=s
  elif t==1:(wm if p>0 else bm)[s&7]|=1<<(s>>4)
  else:
   nm+=V[t]
   if t==3:bc[0 if p>0 else 1]+=1
 h^=ZC[cast]
 if ep>=0:h^=ZE[ep&7]
def parse(u):
 f='abcdefgh'.index(u[0])+(int(u[1])-1)*16
 t='abcdefgh'.index(u[2])+(int(u[3])-1)*16
 pr=0
 if len(u)==5:pr='nbrq'.index(u[4])+2
 return f|t<<7|pr<<14
def uci(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 s='abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[t&7]+str((t>>4)+1)
 return s+'nbrq'[pr-2] if pr else s
def setup(fen,moves):
 global side,cast,ep,half
 for i in range(128):b[i]=0
 stk.clear();rc.clear()
 if moves:fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
 ps=fen.split()
 for r,row in enumerate(ps[0].split('/')):
  rk=7-r;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    p='PNBRQK'.index(ch.upper())+1
    if ch.islower():p=-p
    b[rk*16+f]=p;f+=1
 side=1 if ps[1]=='w' else -1
 cast=0
 if len(ps)>2:
  if 'K' in ps[2]:cast|=1
  if 'Q' in ps[2]:cast|=2
  if 'k' in ps[2]:cast|=4
  if 'q' in ps[2]:cast|=8
 ep=-1
 if len(ps)>3 and ps[3]!='-':ep=(int(ps[3][1])-1)*16+'abcdefgh'.index(ps[3][0])
 half=int(ps[4]) if len(ps)>4 else 0
 scan()
 rc[h]=1
 for u in moves:
  if make(parse(u)):rc[h]=rc.get(h,0)+1
def choose(fen,legal,moves):
 global BG
 setup(fen,moves)
 BG=100000 if nm>4000 else 150000 if nm>1500 else 250000
 if len(tt)>300000:tt.clear()
 ms=[parse(u) for u in legal]
 return uci(root(ms))
def post(p,body):
 req=urllib.request.Request(U+p,data=json.dumps(body).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(req) as r:return json.load(r)
 except urllib.error.HTTPError as e:
  return {"status":"error","code":e.code}
while True:
 g=post("/game",{})
 if g.get("status")=="done":break
 while g.get("status")=="your_move":
  mv=choose(g["fen"],g["legal_moves"],g["moves"])
  r=post("/move",{"game":g["game"],"move":mv})
  if r.get("status")=="error" and g["legal_moves"]:
   r=post("/move",{"game":g["game"],"move":g["legal_moves"][0]})
  g=r
 print(f"game {g.get('game')}: {g.get('outcome')} by {g.get('reason')}",file=sys.stderr)
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
