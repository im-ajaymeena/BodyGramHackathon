# triseps_skinfold=10mm
# subscapular_skinfold=14mm
# supraspinale_skinfold=10mm


from pydantic import BaseModel

class SomatotypeData(BaseModel):
    type: str
    mesomorphy: float
    endomorphy: float
    ectomorphy: float

kayaking = SomatotypeData(
        type="Kayaking",
        endomorphy = 3.38,
        mesomorphy = 3.82,
        ectomorphy = 3.87   
    )

basketball = SomatotypeData(
        type="Basketball",
        endomorphy = 2.77,
        mesomorphy = 4.09,
        ectomorphy = 3.00
    )

football = SomatotypeData(
        type="Football",
        endomorphy = 2.64,
        mesomorphy = 3.57,
        ectomorphy = 3.00
    )

boxing = SomatotypeData(
        type="Boxing",
        endomorphy = 2.3,
        mesomorphy = 3.7,
        ectomorphy = 2.3
    )

somatotype_data_list = [kayaking, basketball, boxing, football] 