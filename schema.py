from pyspark.sql.types import StructType, StructField, StringType

master_schema =  StructType([
    StructField('full_household_identifier',StringType(),True),
    StructField('time_of_interview',StringType(),True),
    StructField('final_outcome_of_survey_code',StringType(),True),
    StructField('type_of_housing_unit_code',StringType(),True),
    StructField('household_type_code',StringType(),True),
    StructField('household_has_telephone_code',StringType(),True),
    StructField('household_can_access_telephone_code',StringType(),True),
    StructField('is_telephone_interview_acceptable_code',StringType(),True),
    StructField('type_of_interview_code',StringType(),True),
    StructField('family_income_range_code',StringType(),True),
    StructField('division_location_code',StringType(),True),
    StructField('race_code',StringType(),True)                 
])




division_location_schema = StructType([
    StructField('div_loc_code',StringType(),False),
    StructField('division_location',StringType(),False)
])

division_location_data = [
    ('1', 'NEW ENGLAND'),
    ('2', 'MIDDLE ATLANTIC'),
    ('3', 'EAST NORTH CENTRAL'),
    ('4', 'WEST NORTH CENTRAL'),
    ('5', 'SOUTH ATLANTIC'),
    ('6', 'EAST SOUTH CENTRAL'),
    ('7', 'WEST SOUTH CENTRAL'),
    ('8', 'MOUNTAIN'),
    ('9', 'PACIFIC')
]




family_income_range_schema = StructType([
    StructField('family_code',StringType(),False),
    StructField('family_income_range',StringType(),False)
])

family_income_range_data = [
    ('1', 'LESS THAN $5,000'),
    ('2', '5,000 TO 7,499'),
    ('3', '7,500 TO 9,999'),
    ('4', '10,000 TO 12,999'),
    ('5', '12,00 TO 14,999'),
    ('6', '15,000 TO 19,999'),
    ('7', '20,000 TO 24,999'),
    ('8', '25,000 TO 29,999'),
    ('9', '30,000 TO 34,'),
    ('10', '35,000 TO 39,999'),
    ('11', '40,000 TO 49,999'),
    ('12', '50,000 TO 59,999'),
    ('13', '60,000 TO 74,999'),
    ('14', '75,000 TO 99,999'),
    ('15', '100,000 TO 149,999'),
    ('16', '150,000 OR MORE')
]




race_schema = StructType([
    StructField('race_code',StringType(),False),
    StructField('race',StringType(),False)
])

race_data = [
    ('01', 'White Only'),
    ('02', 'Black Only'),
    ('03', 'American Indian, Alaskan Native Only'),
    ('04', 'Asian Only'),
    ('05', 'Hawaiian/Pacific Islander Only'),
    ('06', 'White-Black'),
    ('07', 'White-AI'),
    ('08', 'White-Asian'),
    ('09', 'White-HP'),
    ('10', 'Black-AI'),
    ('11', 'Black-Asian'),
    ('12', 'Black-HP'),
    ('13', 'AI-Asian'),
    ('14', 'AI-HP'),
    ('15', 'Asian-HP'),
    ('16', 'W-B-AI'),
    ('17', 'W-B-A'),
    ('18', 'W-B-HP'),
    ('19', 'W-AI-A'),
    ('20', 'W-AI-HP'),
    ('21', 'W-A-HP'),
    ('22', 'B-AI-A'),
    ('23', 'W-B-AI-A'),
    ('24', 'W-AI-A-HP'),
    ('25', 'Other 3 Race Combinations'),
    ('26', 'Other 4 and 5 Race Combinations')
]