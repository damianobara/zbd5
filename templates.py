existsAdQuery = \
"""
query {{
    ad(id: "{id}") {{
        id
    }}
}}
"""

createAdMutation = \
"""
    mutation {{
      createAd(input: {{ad: {{id: "{id}", color: "{color}", hight: {hight}, texts: "{texts}", width: {width} }} }}) {{
        ad {{
          id
        }}
      }}
    }}
"""

updateAdMutation = \
"""
    mutation {{
      updateAd(input: {{patch: {{color: "{color}", hight: {hight}, texts: "{texts}", width: {width} }}, id: "{id}" }}) {{
        ad {{
          id
        }}
      }}
    }}
"""


existsPersonQuery = \
"""
query {{
    person(id: "{id}") {{
        id
    }}
}}
"""

createPersonMutation = \
"""
    mutation {{
      createPerson(input: {{person: {{id: "{id}", gender: "{gender}", birth: "{birth}", income: {income}, interests: {interests}, longitude: {longitude}, latitude: {latitude} }} }}) {{
        person {{
          id
        }}
      }}
    }}
"""

updatePersonMutation = \
"""
    mutation {{
      updatePerson(input: {{patch: {{gender: "{gender}", birth: "{birth}", income: {income}, interests: {interests}, longitude: {longitude}, latitude: {latitude} }}, id: "{id}" }}) {{
        person {{
          id
        }}
      }}
    }}
"""

createViewMutation = \
"""
    mutation {{
      createView(input: {{view: {{personId: "{personId}", adId: "{adId}", viewTime: "{viewTime}" }} }}) {{
        view {{
          personId
          adId
          viewTime
        }}
      }}
    }}
"""
