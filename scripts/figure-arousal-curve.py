import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

INK="#1B2A5B"; ACCENT="#E63B33"; SOFT="#8B6FE0"
f=FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb=FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")

t=np.linspace(0,10,600)
rise=np.clip((t-1.0)/0.9,0,1)**2
fall=np.exp(-np.clip(t-1.9,0,None)/2.6)
y=rise*fall
y=y/y.max()

fig,ax=plt.subplots(figsize=(9,4.6),dpi=200)
ax.plot(t,y,color=ACCENT,lw=5,solid_capstyle="round",zorder=3)
ax.fill_between(t,y,color=ACCENT,alpha=0.07,zorder=1)

for s in ("top","right"): ax.spines[s].set_visible(False)
for s in ("left","bottom"):
    ax.spines[s].set_color(INK); ax.spines[s].set_linewidth(2)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlim(-1.3,10.4); ax.set_ylim(0,1.45)

ax.set_xlabel("tempo", fontproperties=f, fontsize=14, color=INK, labelpad=10)
ax.set_ylabel("activação", fontproperties=f, fontsize=14, color=INK, labelpad=12)

peak=t[np.argmax(y)]
event=1.0

ax.text(2.1,1.20,"sobe depressa",fontproperties=fb,fontsize=15,color=ACCENT,
        ha="left",va="bottom")
ax.text(5.8,0.62,"desce devagar",fontproperties=fb,fontsize=15,color=ACCENT,
        ha="left",va="bottom")

ax.axvline(event,0,1.02/1.42,color=INK,lw=1.4,ls=(0,(4,4)),alpha=0.5,zorder=2)
ax.text(event-0.15,1.06,"acontece\nalguma coisa",fontproperties=f,fontsize=13,
        color=INK,ha="right",va="bottom",linespacing=1.35)
ax.annotate("",xy=(2.0,1.24),xytext=(1.25,1.02),
            arrowprops=dict(arrowstyle="-",lw=1.6,color=ACCENT,alpha=0.6,
                            connectionstyle="arc3,rad=-0.25"))

ax.text(6.6,0.30,"aqui a estratégia ainda está a agir,\nmesmo que ela ache que não",
        fontproperties=f,fontsize=12,color=SOFT,ha="left",va="bottom",
        linespacing=1.4)

ax.text(0,-0.30,"Esquema ilustrativo. Não representa medições.",
        transform=ax.transAxes,fontproperties=f,fontsize=11,color="#7A839B")

plt.tight_layout()
plt.savefig("curva.png",bbox_inches="tight",facecolor="white")
print("ok")
