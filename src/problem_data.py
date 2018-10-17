import go_benchmark_functions as gbf
import numpy as np
import random
import math


fs = {}
fs['Ackley01'] = gbf.Ackley01
fs['Ackley02'] = gbf.Ackley02
fs['Ackley03'] = gbf.Ackley03
fs['Adjiman'] = gbf.Adjiman
fs['Alpine01'] = gbf.Alpine01
fs['Alpine02'] = gbf.Alpine02
fs['AMGM'] = gbf.AMGM
fs['BartelsConn'] = gbf.BartelsConn
fs['Beale'] = gbf.Beale
fs['BiggsExp02'] = gbf.BiggsExp02
fs['BiggsExp03'] = gbf.BiggsExp03
fs['BiggsExp04'] = gbf.BiggsExp04
fs['BiggsExp05'] = gbf.BiggsExp05
fs['Bird'] = gbf.Bird
fs['Bohachevsky1'] = gbf.Bohachevsky1
fs['Bohachevsky2'] = gbf.Bohachevsky2
fs['Bohachevsky3'] = gbf.Bohachevsky3
fs['BoxBetts'] = gbf.BoxBetts
fs['Branin01'] = gbf.Branin01
fs['Branin02'] = gbf.Branin02
fs['Brent'] = gbf.Brent
fs['Brown'] = gbf.Brown
fs['Bukin02'] = gbf.Bukin02
fs['Bukin04'] = gbf.Bukin04
fs['Bukin06'] = gbf.Bukin06
fs['CarromTable'] = gbf.CarromTable
fs['Chichinadze'] = gbf.Chichinadze
fs['Cigar'] = gbf.Cigar
fs['Cola'] = gbf.Cola
fs['Colville'] = gbf.Colville
fs['Corana'] = gbf.Corana
fs['CosineMixture'] = gbf.CosineMixture
fs['CrossInTray'] = gbf.CrossInTray
fs['CrossLegTable'] = gbf.CrossLegTable
fs['CrownedCross'] = gbf.CrownedCross
fs['Csendes'] = gbf.Csendes
fs['Cube'] = gbf.Cube
fs['Damavandi'] = gbf.Damavandi
fs['Deb01'] = gbf.Deb01
fs['Deb03'] = gbf.Deb03
fs['Decanomial'] = gbf.Decanomial
fs['Deceptive'] = gbf.Deceptive
fs['DeckkersAarts'] = gbf.DeckkersAarts
fs['DeflectedCorrugatedSpring'] = gbf.DeflectedCorrugatedSpring
fs['DeVilliersGlasser01'] = gbf.DeVilliersGlasser01
fs['DeVilliersGlasser02'] = gbf.DeVilliersGlasser02
fs['DixonPrice'] = gbf.DixonPrice
fs['Dolan'] = gbf.Dolan
fs['DropWave'] = gbf.DropWave
fs['Easom'] = gbf.Easom
fs['Eckerle4'] = gbf.Eckerle4
fs['EggCrate'] = gbf.EggCrate
fs['EggHolder'] = gbf.EggHolder
fs['ElAttarVidyasagarDutta'] = gbf.ElAttarVidyasagarDutta
fs['Exp2'] = gbf.Exp2
fs['Exponential'] = gbf.Exponential
fs['FreudensteinRoth'] = gbf.FreudensteinRoth
fs['Gear'] = gbf.Gear
fs['Giunta'] = gbf.Giunta
fs['GoldsteinPrice'] = gbf.GoldsteinPrice
fs['Griewank'] = gbf.Griewank
fs['Gulf'] = gbf.Gulf
fs['Hansen'] = gbf.Hansen
fs['Hartmann3'] = gbf.Hartmann3
fs['Hartmann6'] = gbf.Hartmann6
fs['HelicalValley'] = gbf.HelicalValley
fs['HimmelBlau'] = gbf.HimmelBlau
fs['HolderTable'] = gbf.HolderTable
fs['Hosaki'] = gbf.Hosaki
fs['Infinity'] = gbf.Infinity
fs['JennrichSampson'] = gbf.JennrichSampson
fs['Judge'] = gbf.Judge
fs['Katsuura'] = gbf.Katsuura
fs['Keane'] = gbf.Keane
fs['Kowalik'] = gbf.Kowalik
fs['Langermann'] = gbf.Langermann
fs['LennardJones'] = gbf.LennardJones
fs['Leon'] = gbf.Leon
fs['Levy03'] = gbf.Levy03
fs['Levy05'] = gbf.Levy05
fs['Levy13'] = gbf.Levy13
fs['Matyas'] = gbf.Matyas
fs['McCormick'] = gbf.McCormick
fs['Meyer'] = gbf.Meyer
fs['Michalewicz'] = gbf.Michalewicz
fs['MieleCantrell'] = gbf.MieleCantrell
fs['Mishra01'] = gbf.Mishra01
fs['Mishra02'] = gbf.Mishra02
fs['Mishra03'] = gbf.Mishra03
fs['Mishra04'] = gbf.Mishra04
fs['Mishra05'] = gbf.Mishra05
fs['Mishra06'] = gbf.Mishra06
fs['Mishra07'] = gbf.Mishra07
fs['Mishra08'] = gbf.Mishra08
fs['Mishra09'] = gbf.Mishra09
fs['Mishra10'] = gbf.Mishra10
fs['Mishra11'] = gbf.Mishra11
fs['MultiModal'] = gbf.MultiModal
fs['NeedleEye'] = gbf.NeedleEye
fs['NewFunction01'] = gbf.NewFunction01
fs['NewFunction02'] = gbf.NewFunction02
fs['OddSquare'] = gbf.OddSquare
fs['Parsopoulos'] = gbf.Parsopoulos
fs['Pathological'] = gbf.Pathological
fs['Paviani'] = gbf.Paviani
fs['Penalty01'] = gbf.Penalty01
fs['Penalty02'] = gbf.Penalty02
fs['PenHolder'] = gbf.PenHolder
fs['PermFunction01'] = gbf.PermFunction01
fs['PermFunction02'] = gbf.PermFunction02
fs['Pinter'] = gbf.Pinter
fs['Plateau'] = gbf.Plateau
fs['Powell'] = gbf.Powell
fs['PowerSum'] = gbf.PowerSum
fs['Price01'] = gbf.Price01
fs['Price02'] = gbf.Price02
fs['Price03'] = gbf.Price03
fs['Price04'] = gbf.Price04
fs['Qing'] = gbf.Qing
fs['Quadratic'] = gbf.Quadratic
fs['Quintic'] = gbf.Quintic
fs['Rana'] = gbf.Rana
fs['Rastrigin'] = gbf.Rastrigin
fs['Ratkowsky01'] = gbf.Ratkowsky01
fs['Ratkowsky02'] = gbf.Ratkowsky02
fs['Ripple01'] = gbf.Ripple01
fs['Ripple25'] = gbf.Ripple25
fs['Rosenbrock'] = gbf.Rosenbrock
fs['RosenbrockModified'] = gbf.RosenbrockModified
fs['RotatedEllipse01'] = gbf.RotatedEllipse01
fs['RotatedEllipse02'] = gbf.RotatedEllipse02
fs['Salomon'] = gbf.Salomon
fs['Sargan'] = gbf.Sargan
fs['Schaffer01'] = gbf.Schaffer01
fs['Schaffer02'] = gbf.Schaffer02
fs['Schaffer03'] = gbf.Schaffer03
fs['Schaffer04'] = gbf.Schaffer04
fs['Schwefel01'] = gbf.Schwefel01
fs['Schwefel02'] = gbf.Schwefel02
fs['Schwefel04'] = gbf.Schwefel04
fs['Schwefel06'] = gbf.Schwefel06
fs['Schwefel20'] = gbf.Schwefel20
fs['Schwefel21'] = gbf.Schwefel21
fs['Schwefel22'] = gbf.Schwefel22
fs['Schwefel26'] = gbf.Schwefel26
fs['Schwefel36'] = gbf.Schwefel36
fs['Shekel05'] = gbf.Shekel05
fs['Shekel07'] = gbf.Shekel07
fs['Shekel10'] = gbf.Shekel10
fs['Shubert01'] = gbf.Shubert01
fs['Shubert03'] = gbf.Shubert03
fs['Shubert04'] = gbf.Shubert04
fs['SineEnvelope'] = gbf.SineEnvelope
fs['SixHumpCamel'] = gbf.SixHumpCamel
fs['Sodp'] = gbf.Sodp
fs['Sphere'] = gbf.Sphere
fs['Step'] = gbf.Step
fs['Step2'] = gbf.Step2
fs['Stochastic'] = gbf.Stochastic
fs['StretchedV'] = gbf.StretchedV
fs['StyblinskiTang'] = gbf.StyblinskiTang
fs['TestTubeHolder'] = gbf.TestTubeHolder
fs['Thurber'] = gbf.Thurber
fs['Treccani'] = gbf.Treccani
fs['Trefethen'] = gbf.Trefethen
fs['ThreeHumpCamel'] = gbf.ThreeHumpCamel
fs['Trid'] = gbf.Trid
fs['Trigonometric01'] = gbf.Trigonometric01
fs['Trigonometric02'] = gbf.Trigonometric02
fs['Tripod'] = gbf.Tripod
fs['Ursem01'] = gbf.Ursem01
fs['Ursem03'] = gbf.Ursem03
fs['Ursem04'] = gbf.Ursem04
fs['UrsemWaves'] = gbf.UrsemWaves
fs['VenterSobiezcczanskiSobieski'] = gbf.VenterSobiezcczanskiSobieski
fs['Vincent'] = gbf.Vincent
fs['Watson'] = gbf.Watson
fs['Wavy'] = gbf.Wavy
fs['WayburnSeader01'] = gbf.WayburnSeader01
fs['WayburnSeader02'] = gbf.WayburnSeader02
fs['Weierstrass'] = gbf.Weierstrass
fs['Whitley'] = gbf.Whitley
fs['Wolfe'] = gbf.Wolfe
fs['XinSheYang01'] = gbf.XinSheYang01
fs['XinSheYang02'] = gbf.XinSheYang02
fs['XinSheYang03'] = gbf.XinSheYang03
fs['XinSheYang04'] = gbf.XinSheYang04
fs['Xor'] = gbf.Xor
fs['YaoLiu04'] = gbf.YaoLiu04
fs['YaoLiu09'] = gbf.YaoLiu09
fs['Zacharov'] = gbf.Zacharov
fs['ZeroSum'] = gbf.ZeroSum
fs['Zettl'] = gbf.Zettl
fs['Zimmerman'] = gbf.Zimmerman
fs['Zirilli'] = gbf.Zirilli


class ProblemData:
    def __init__(self, pname=None, n_dimensions=None):
        self.pname = pname

        self.f_pointer = fs[self.pname](dimensions=n_dimensions)

        self.n_dimensions = n_dimensions

    def eval(self, vector):
        return self.f_pointer(vector)