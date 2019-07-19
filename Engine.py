def engine(self):
    name=""
    Configuration=""
    Production=""
    stroke=""
    bore=""
    Compression_ratio=""
    Displacement=""
    HP=""
    Torque=""
    Redline=""
    
    def load(self,nam,config,prod,stro,bor,comp,disp,bhp,ftlbs,rpm):
        self.name = nam
        self.Configuration = config
        self.Production = prod
        self.stroke = stro
        self.bore = bor
        self.Compression_ratio = comp
        self.Displacement = disp
        self.HP = bhp
        self.Torque = ftlbs
        self.Redline = rpm
        return True

