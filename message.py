def create_message(payload):
  user = payload['user_block']['plain_input']['value']
  
  message = [		{
			"color": "#D44500",
			"blocks": [
      {
			  "type": "section",
			  "text": {
			  	"type": "mrkdwn",
			  	"text": "New order from *" + user + "*"
			          }
		  }]
    }
  ]
  
  oatmeal_options = payload['oatmeal_block']['checkboxes-action']['selected_options']
  oatmeal = []
  
  if oatmeal_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oatmeal*"
			}
		})
    
    for selected_options in oatmeal_options:
      oatmeal.append(selected_options['text']['text'])
      
    for item in oatmeal:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  nut_options = payload['nuts_block']['checkboxes-action']['selected_options']
  nuts = []
  if nut_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Nuts*"
			}
		})
    for selected_options in nut_options:
      nuts.append(selected_options['text']['text']) 
      
    for item in nuts:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  jerky_options = payload['jerky_block']['checkboxes-action']['selected_options']
  jerky = []
  if jerky_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Jerky Sticks*"
			}
		})
    for selected_options in jerky_options:
      jerky.append(selected_options['text']['text']) 
      
    for item in jerky:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
      
  honey_stinger_options = payload['honey_block']['checkboxes-action']['selected_options']
  honey_stinger = []
  if honey_stinger_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Honey Stinger*"
			}
		})
    for selected_options in honey_stinger_options:
      honey_stinger.append(selected_options['text']['text']) 
      
    for item in honey_stinger:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
      
  libre_naturels_options = payload['libre_block']['checkboxes-action']['selected_options']
  libre_naturels = []
  if libre_naturels_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Libre Naturels*"
			}
		})
    for selected_options in libre_naturels_options:
      libre_naturels.append(selected_options['text']['text']) 
    for item in libre_naturels:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  breakfast_bar_options = payload['breakfast_bar_block']['checkboxes-action']['selected_options']
  breakfast_bar = []
  if breakfast_bar_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oatmeal Breakfast Bars*"
			}
		})
    for selected_options in breakfast_bar_options:
      breakfast_bar.append(selected_options['text']['text']) 
    for item in breakfast_bar:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  rxbars_options = payload['rxBar_block']['checkboxes-action']['selected_options']
  rxbars = []
  if rxbars_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*RxBars*"
			}
		})
    for selected_options in rxbars_options:
      rxbars.append(selected_options['text']['text']) 
    for item in rxbars:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  milk_options = payload['milk_block']['checkboxes-action']['selected_options']
  milk =[]
  if milk_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Milk*"
			}
		})
    for selected_options in milk_options:
      milk.append(selected_options['text']['text']) 
    for item in milk:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  protein_shake_options = payload['protein_shake_block']['checkboxes-action']['selected_options']
  protein_shakes = []
  if protein_shake_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Protein Shakes*"
			}
		})
    for selected_options in protein_shake_options:
      protein_shakes.append(selected_options['text']['text']) 
    for item in protein_shakes:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  yogurt_hummus_options = payload['yogurt_block']['checkboxes-action']['selected_options']
  yogurt_hummus = []
  if yogurt_hummus_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Yogurt & Hummus*"
			}
		})
    for selected_options in yogurt_hummus_options:
      yogurt_hummus.append(selected_options['text']['text']) 
    for item in yogurt_hummus:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  fruit_veggies_options = payload['fruit_block']['checkboxes-action']['selected_options']
  fruit_veggies = []
  if fruit_veggies_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Fruits & Veggies*"
			}
		})
    for selected_options in fruit_veggies_options:
      fruit_veggies.append(selected_options['text']['text']) 
    for item in fruit_veggies:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  groceries_options = payload['grocery_block']['checkboxes-action']['selected_options']
  groceries = []
  if groceries_options:
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Grocery Items*"
			}
		})
    for selected_options in groceries_options:
      groceries.append(selected_options['text']['text']) 
    for item in groceries:
      message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + item,
				"emoji": True
			  }
		  })
  
  requests = payload['requests_block']['plain_text_input-action']['value']
  if requests is not None :
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Requests*"
			}
		})
    message[0]['blocks'].append({
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "" + requests,
				"emoji": True
			  }
		  })
 
  return message