# Importaciones de Matplotlib
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
# Definir el colormap personalizado
# Definir los colores en RGB
rgb = {'red': ((0.0, 0.0, 0.0),
                (0.5, 1.0, 1.0),
                (1.0, 1.0, 1.0)),

        'green': ((0.0, 0.0, 0.0),
                    (0.5, 1.0, 1.0),
                    (1.0, 0.0, 0.0)),

        'blue': ((0.0, 1.0, 1.0),
                (0.5, 1.0, 1.0),
                (1.0, 0.0, 0.0))
        }
# Definir el colormap
cmap_ = LinearSegmentedColormap('RedGreenBlue', rgb)

# Actualización de los parámetros de Matplotlib
gris = '#757575'
mpl.rcParams.update(
    {
        'figure.constrained_layout.use': True,
        'interactive': False,
        "text.usetex": False,  # Use mathtext, not LaTeX
        "font.family": "cmr10",  # Use the Computer modern font
        "mathtext.fontset": "cm",
        "axes.formatter.use_mathtext": True,
        "axes.unicode_minus": False,
        "text.color": gris,
        "font.size": 12,
        "xtick.color": gris,
        "ytick.color": gris,
        "axes.labelcolor": gris,
        "axes.edgecolor": gris,
        "axes.spines.right": False,
        "axes.spines.top": False
    }
)

