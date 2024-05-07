# streamlit_pets

**Streamlit App link:** https://apppets-awmlsjbqvxef3udkzbbmmx.streamlit.app/  
  **Introduction:** This App explores shelter pet outcomes from Long Beach Animal shelter from 2017 to 2024  
  **Data/operation abstraction design:**
This dataset was downloaded from [data.longbeach.gov](https://data.longbeach.gov/explore/dataset/animal-shelter-intakes-and-outcomes/information/?flg=en-us&disjunctive.animal_type&disjunctive.primary_color&disjunctive.sex&disjunctive.intake_cond&disjunctive.intake_type&disjunctive.reason&disjunctive.outcome_type&disjunctive.outcome_subtype&disjunctive.intake_is_dead&disjunctive.outcome_is_dead).
It contained several null values that were dropped. The "Sex" column was also split into two new columns, "gender" and "spay/neuter."   
  **Future work:** The plan for future work is to focus the analysis solely on adoption and euthanasia outcomes to determine if there are any interesting trends among those outcomes. 
