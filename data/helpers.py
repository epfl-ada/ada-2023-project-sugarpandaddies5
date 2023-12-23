#This function was written with the help of Chat GPT 
#This function takes the title and the year of release of a movie, and do a request to obtain WIkipedia Page ID
import requests

def get_wikipedia_page_id(movie_title, release_year):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={movie_title} {release_year}"
    
    headers = {
        'User-Agent': 'Your-User-Agent-String',  # Replace with a user-agent string of your choice
    }

    response = requests.get(search_url, headers=headers)
    data = response.json()

    if 'query' in data and 'search' in data['query']:
        search_results = data['query']['search']
        if search_results:
            # Assuming the first search result is the most relevant
            first_result = search_results[0]
            page_id = first_result['pageid']
            return page_id

    return None

## Function that returns the production company found on the Wikipedia page of a movie, when given the wikipedia page ID
#This function was done with the help of ChatGPT

def get_entity_label(entity_id):
    # API endpoint URL for fetching labels of the specified entity
    entity_label_url = f'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=labels&languages=en&ids={entity_id}'

    try:
        # Make the API request
        entity_label_response = requests.get(entity_label_url)
        entity_label_response.raise_for_status()

        # Parse the JSON response
        entity_label_data = entity_label_response.json()

        # Extract the label from the response
        if 'labels' in entity_label_data['entities'][entity_id]:
            label = entity_label_data['entities'][entity_id]['labels']['en']['value']
            return label

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

    return None



def get_production_company(wikipedia_page_id):
    # Replace 'YOUR_USER_AGENT' with an appropriate user agent string
    headers = {'User-Agent': 'YOUR_USER_AGENT'}

    # API endpoint URL for fetching details about the Wikidata item associated with the Wikipedia page
    wikidata_url = f'https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&format=json&pageids={wikipedia_page_id}'

    try:
        # Make the API request to get the Wikidata item associated with the Wikipedia page
        wikidata_response = requests.get(wikidata_url, headers=headers)
        wikidata_response.raise_for_status()

        # Parse the JSON response
        wikidata_data = wikidata_response.json()

        # Extract the Wikidata item ID from the response
        wikidata_item_id = wikidata_data['query']['pages'][str(wikipedia_page_id)].get('pageprops', {}).get('wikibase_item')

        if wikidata_item_id:
            # Now, fetch information about the Wikidata item, including production company details
            wikidata_item_url = f'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=claims&ids={wikidata_item_id}'
            wikidata_item_response = requests.get(wikidata_item_url, headers=headers)
            wikidata_item_response.raise_for_status()

            # Parse the JSON response
            wikidata_item_data = wikidata_item_response.json()

            # Extract production company information from the response
            if 'claims' in wikidata_item_data['entities'][wikidata_item_id]:
                claims = wikidata_item_data['entities'][wikidata_item_id]['claims']
                if 'P272' in claims:  # Assuming P272 is the property for production company
                    production_company_id = claims['P272'][0]['mainsnak']['datavalue']['value']['id']
                    
                    # Fetch production company name using another API request
                    production_company_name = get_entity_label(production_company_id)
                    
                    return production_company_name

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

    return None