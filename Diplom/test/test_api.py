import pytest
import allure
import requests

from pages.api_page import ProjectAPI
@allure.title("Пассажир 1 взрослый")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")

def test_post_avia(): #Билет в 1 сторону, 1 взрослый
    data = {
    "search": {
        "id": "93734318-dd3d-4b13-8ed7-159125e2ad02",
        "ticket": {
            "sort_rating": 0,
            "segments": [
                {
                    "flights": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ],
                    "transfers": [
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": True,
                            "tags": [
                                "overnight_layover"
                            ],
                            "arrival_airport": "SVO",
                            "departure_airport": "SVO",
                            "departure_airline": "DP",
                            "arrival_airline": "DP",
                            "duration": 1960,
                            "country_code": "RU",
                            "city_code": "MOW"
                        }
                    ]
                }
            ],
            "is_direct": False,
            "max_stops": 1,
            "min_stop_duration": 1960,
            "max_stop_duration": 1960,
            "segments_time": [
                [
                    1745013000,
                    1745142000
                ]
            ],
            "segment_durations": [
                2150
            ],
            "total_duration": 2150,
            "segments_airports": [
                [
                    "CSY",
                    "KZN"
                ]
            ],
            "carriers": [
                "DP"
            ],
            "hashsum": "a84cf5f36375a5ac",
            "sign": "aa911b7c7e644f0dcf40d539d0eb8a34",
            "tags": [
                "has_night_transfer",
                "long_layover",
                "night_transfer",
                "overnight_layover"
            ],
            "badges": [],
            "debug": {
                "agent_id": 70,
                "popularity": 0
            },
            "extra_fares": {
                "H1|L0|CH1|R0|TBC0": [
                    {
                        "proposal_id": "70:202",
                        "index": 0
                    }
                ]
            },
            "score": 0.0036976909661849814,
            "position": None,
            "segment": [
                {
                    "flight": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ]
                }
            ],
            "terms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 7419,
                    "pricePerPerson": 7419,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 7419,
                    "searchPrice": 7419,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.026636433585321525,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:202",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 7419,
                    "is_charter": False,
                    "url": "70:202"
                }
            },
            "xterms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 7419,
                    "pricePerPerson": 7419,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 7419,
                    "searchPrice": 7419,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.026636433585321525,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:202",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 7419,
                    "is_charter": False,
                    "url": "70:202"
                }
            }
        },
        "search_params": {
            "precheckedFilters": {},
            "destinationCountryIata": "RU",
            "destinationCityIata": "KZN",
            "originCountryIata": "RU",
            "originCityIata": "CSY",
            "isOneWay": True,
            "isPlacesRestored": True,
            "paymentMethod": "all",
            "passengers": {
                "adults": 1,
                "children": 0,
                "infants": 0
            },
            "segments": [
                {
                    "origin": "CSY",
                    "original_origin": "CSY",
                    "origin_country": "RU",
                    "origin_type": "city",
                    "destination": "KZN",
                    "original_destination": "KZN",
                    "destination_country": "RU",
                    "destination_type": "city",
                    "date": "2025-04-18",
                    "origin_name": "Чебоксары",
                    "destination_name": "Казань",
                    "originType": "city",
                    "destinationType": "city"
                }
            ],
            "startSearch": True,
            "tripClass": "Y",
            "tripType": "oneway",
            "trip_class": "Y",
            "with_request": False,
            "originName": "Чебоксары",
            "destinationName": "Казань",
            "locale": "ru",
            "host": "search.aviasales.ru",
            "currency": "rub",
            "market": "ru",
            "formParams": {
                "passengers": {
                    "adults": 1,
                    "children": 0,
                    "infants": 0
                },
                "tripClass": "Y",
                "segments": [
                    {
                        "origin": {
                            "iata": "CSY",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "destination": {
                            "iata": "KZN",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "date": "2025-04-17T21:00:00.000Z"
                    }
                ],
                "paymentMethod": "all"
            }
        }
    }
}
    if response is not None:
     print(response.status_code)
    else:
     print("Ответ отсутствует.")
    response = test_post_avia()
    assert response.status_code == 200   


@allure.title("Пассажир 1 взрослый. В обе стороны")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в обе стороны.")
@allure.severity("critical")

def test_post_avia_2(): #Билет в обе стороны, 1 взрослый

   data = {
    "search": {
        "id": "53383e5a-a379-43e3-a6e1-4210a057bc03",
        "ticket": {
            "sort_rating": 0,
            "segments": [
                {
                    "flights": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-19",
                            "arrival_time": "09:15",
                            "arrival_timestamp": 1745043300,
                            "departure": "SVO",
                            "departure_date": "2025-04-19",
                            "departure_time": "07:40",
                            "departure_timestamp": 1745037600,
                            "duration": 95,
                            "local_arrival_timestamp": 1745054100,
                            "local_departure_timestamp": 1745048400,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 500,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745048400:1745054100:SVO:KZN"
                        }
                    ],
                    "transfers": [
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": True,
                            "tags": [
                                "overnight_layover"
                            ],
                            "arrival_airport": "SVO",
                            "departure_airport": "SVO",
                            "departure_airline": "DP",
                            "arrival_airline": "DP",
                            "duration": 500,
                            "country_code": "RU",
                            "city_code": "MOW"
                        }
                    ]
                },
                {
                    "flights": [
                        {
                            "arrival": "KVX",
                            "arrival_date": "2025-04-19",
                            "arrival_time": "16:40",
                            "arrival_timestamp": 1745070000,
                            "departure": "KZN",
                            "departure_date": "2025-04-19",
                            "departure_time": "15:50",
                            "departure_timestamp": 1745067000,
                            "duration": 50,
                            "local_arrival_timestamp": 1745080800,
                            "local_departure_timestamp": 1745077800,
                            "number": "519",
                            "operating_carrier": "RT",
                            "airline_id": "RT",
                            "aircraft": "Canadair CRJ 200",
                            "equipment": "CR2",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745077800:1745080800:KZN:KVX"
                        },
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-19",
                            "arrival_time": "23:30",
                            "arrival_timestamp": 1745094600,
                            "departure": "KVX",
                            "departure_date": "2025-04-19",
                            "departure_time": "21:45",
                            "departure_timestamp": 1745088300,
                            "duration": 105,
                            "local_arrival_timestamp": 1745105400,
                            "local_departure_timestamp": 1745099100,
                            "number": "6820",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 305,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745099100:1745105400:KVX:SVO"
                        },
                        {
                            "arrival": "CSY",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:30",
                            "arrival_timestamp": 1745130600,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:05",
                            "departure_timestamp": 1745125500,
                            "duration": 85,
                            "local_arrival_timestamp": 1745141400,
                            "local_departure_timestamp": 1745136300,
                            "number": "6807",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 515,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136300:1745141400:SVO:CSY"
                        }
                    ],
                    "transfers": [
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": False,
                            "tags": [],
                            "arrival_airport": "KVX",
                            "departure_airport": "KVX",
                            "departure_airline": "DP",
                            "arrival_airline": "RT",
                            "duration": 305,
                            "country_code": "RU",
                            "city_code": "KVX"
                        },
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": True,
                            "tags": [
                                "overnight_layover"
                            ],
                            "arrival_airport": "SVO",
                            "departure_airport": "SVO",
                            "departure_airline": "DP",
                            "arrival_airline": "DP",
                            "duration": 515,
                            "country_code": "RU",
                            "city_code": "MOW"
                        }
                    ]
                }
            ],
            "is_direct": False,
            "max_stops": 2,
            "min_stop_duration": 305,
            "max_stop_duration": 515,
            "segments_time": [
                [
                    1745013000,
                    1745054100
                ],
                [
                    1745077800,
                    1745141400
                ]
            ],
            "segment_durations": [
                685,
                1060
            ],
            "total_duration": 1745,
            "segments_airports": [
                [
                    "CSY",
                    "KZN"
                ],
                [
                    "KZN",
                    "CSY"
                ]
            ],
            "carriers": [
                "DP",
                "RT"
            ],
            "hashsum": "e97904f9a8df4217",
            "sign": "a03e80ebd54b231d7b06b5a438fe2484",
            "tags": [
                "has_night_transfer",
                "long_layover",
                "night_transfer",
                "overnight_layover"
            ],
            "badges": [],
            "debug": {
                "agent_id": 70,
                "popularity": 0
            },
            "extra_fares": {
                "H1|L0|CH1|R0|TBC0": [
                    {
                        "proposal_id": "70:1081",
                        "index": 0
                    }
                ]
            },
            "score": 0.0010823475285006653,
            "position": None,
            "segment": [
                {
                    "flight": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-19",
                            "arrival_time": "09:15",
                            "arrival_timestamp": 1745043300,
                            "departure": "SVO",
                            "departure_date": "2025-04-19",
                            "departure_time": "07:40",
                            "departure_timestamp": 1745037600,
                            "duration": 95,
                            "local_arrival_timestamp": 1745054100,
                            "local_departure_timestamp": 1745048400,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 500,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745048400:1745054100:SVO:KZN"
                        }
                    ]
                },
                {
                    "flight": [
                        {
                            "arrival": "KVX",
                            "arrival_date": "2025-04-19",
                            "arrival_time": "16:40",
                            "arrival_timestamp": 1745070000,
                            "departure": "KZN",
                            "departure_date": "2025-04-19",
                            "departure_time": "15:50",
                            "departure_timestamp": 1745067000,
                            "duration": 50,
                            "local_arrival_timestamp": 1745080800,
                            "local_departure_timestamp": 1745077800,
                            "number": "519",
                            "operating_carrier": "RT",
                            "airline_id": "RT",
                            "aircraft": "Canadair CRJ 200",
                            "equipment": "CR2",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745077800:1745080800:KZN:KVX"
                        },
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-19",
                            "arrival_time": "23:30",
                            "arrival_timestamp": 1745094600,
                            "departure": "KVX",
                            "departure_date": "2025-04-19",
                            "departure_time": "21:45",
                            "departure_timestamp": 1745088300,
                            "duration": 105,
                            "local_arrival_timestamp": 1745105400,
                            "local_departure_timestamp": 1745099100,
                            "number": "6820",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 305,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745099100:1745105400:KVX:SVO"
                        },
                        {
                            "arrival": "CSY",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:30",
                            "arrival_timestamp": 1745130600,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:05",
                            "departure_timestamp": 1745125500,
                            "duration": 85,
                            "local_arrival_timestamp": 1745141400,
                            "local_departure_timestamp": 1745136300,
                            "number": "6807",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 515,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136300:1745141400:SVO:CSY"
                        }
                    ]
                }
            ],
            "terms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 20840,
                    "pricePerPerson": 20840,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 20840,
                    "searchPrice": 20840,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 5,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "virtual_interline_domestic"
                    ],
                    "id": "70:1081",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "KECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ],
                        [
                            {
                                "fareCode": "PCOW",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "RT",
                                    "airlineId": "RT",
                                    "number": "519"
                                },
                                "baggage": {
                                    "count": 1,
                                    "weight": 10
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 5,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": True
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "OALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6820"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "NECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6807"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ],
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            },
                            {
                                "isVirtualInterline": False,
                                "tags": []
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 4,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 5,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 20840,
                    "is_charter": False,
                    "url": "70:1081"
                }
            },
            "xterms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 20840,
                    "pricePerPerson": 20840,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 20840,
                    "searchPrice": 20840,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 5,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "virtual_interline_domestic"
                    ],
                    "id": "70:1081",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "KECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ],
                        [
                            {
                                "fareCode": "PCOW",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "RT",
                                    "airlineId": "RT",
                                    "number": "519"
                                },
                                "baggage": {
                                    "count": 1,
                                    "weight": 10
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 5,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": True
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "OALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6820"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "NECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6807"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 4,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ],
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            },
                            {
                                "isVirtualInterline": False,
                                "tags": []
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 4,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 5,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 20840,
                    "is_charter": False,
                    "url": "70:1081"
                }
            }
        },
        "search_params": {
            "precheckedFilters": {},
            "destinationCountryIata": "RU",
            "destinationCityIata": "KZN",
            "originCountryIata": "RU",
            "originCityIata": "CSY",
            "isOneWay": False,
            "isPlacesRestored": True,
            "paymentMethod": "all",
            "passengers": {
                "adults": 1,
                "children": 0,
                "infants": 0
            },
            "segments": [
                {
                    "origin": "CSY",
                    "original_origin": "CSY",
                    "origin_country": "RU",
                    "origin_type": "city",
                    "destination": "KZN",
                    "original_destination": "KZN",
                    "destination_country": "RU",
                    "destination_type": "city",
                    "date": "2025-04-18",
                    "origin_name": "Чебоксары",
                    "destination_name": "Казань",
                    "originType": "city",
                    "destinationType": "city"
                },
                {
                    "origin": "KZN",
                    "original_origin": "KZN",
                    "origin_country": "RU",
                    "origin_type": "city",
                    "destination": "CSY",
                    "original_destination": "CSY",
                    "destination_country": "RU",
                    "destination_type": "city",
                    "date": "2025-04-19",
                    "origin_name": "Казань",
                    "destination_name": "Чебоксары",
                    "originType": "city",
                    "destinationType": "city"
                }
            ],
            "startSearch": True,
            "tripClass": "Y",
            "tripType": "roundtrip",
            "trip_class": "Y",
            "with_request": False,
            "originName": "Чебоксары",
            "destinationName": "Казань",
            "locale": "ru",
            "host": "search.aviasales.ru",
            "currency": "rub",
            "market": "ru",
            "formParams": {
                "passengers": {
                    "adults": 1,
                    "children": 0,
                    "infants": 0
                },
                "tripClass": "Y",
                "segments": [
                    {
                        "origin": {
                            "iata": "CSY",
                            "name": "Чебоксары",
                            "type": "city",
                            "weight": 15215,
                            "cases": {
                                "vi": "в Чебоксары",
                                "tv": "Чебоксарами",
                                "su": "Чебоксары",
                                "ro": "Чебоксар",
                                "pr": "Чебоксарах",
                                "da": "Чебоксарам"
                            },
                            "countryIata": "RU",
                            "countryName": "Россия",
                            "coordinates": {
                                "lon": 47.266666,
                                "lat": 56.13333
                            }
                        },
                        "destination": {
                            "iata": "KZN",
                            "name": "Казань",
                            "type": "city",
                            "weight": 165113,
                            "cases": {
                                "vi": "в Казань",
                                "tv": "Казанью",
                                "su": "Казань",
                                "ro": "Казани",
                                "pr": "Казани",
                                "da": "Казани"
                            },
                            "countryIata": "RU",
                            "countryName": "Россия",
                            "coordinates": {
                                "lon": 49.29824,
                                "lat": 55.60844
                            }
                        },
                        "date": "2025-04-17T21:00:00.000Z"
                    },
                    {
                        "origin": {
                            "iata": "KZN",
                            "name": "Казань",
                            "type": "city",
                            "weight": 165113,
                            "cases": {
                                "vi": "в Казань",
                                "tv": "Казанью",
                                "su": "Казань",
                                "ro": "Казани",
                                "pr": "Казани",
                                "da": "Казани"
                            },
                            "countryIata": "RU",
                            "countryName": "Россия",
                            "coordinates": {
                                "lon": 49.29824,
                                "lat": 55.60844
                            }
                        },
                        "destination": {
                            "iata": "CSY",
                            "name": "Чебоксары",
                            "type": "city",
                            "weight": 15215,
                            "cases": {
                                "vi": "в Чебоксары",
                                "tv": "Чебоксарами",
                                "su": "Чебоксары",
                                "ro": "Чебоксар",
                                "pr": "Чебоксарах",
                                "da": "Чебоксарам"
                            },
                            "countryIata": "RU",
                            "countryName": "Россия",
                            "coordinates": {
                                "lon": 47.266666,
                                "lat": 56.13333
                            }
                        },
                        "date": "2025-04-18T21:00:00.000Z"
                    }
                ],
                "paymentMethod": "all"
            }
        }
    }
}
   if response is not None:
     print(response.status_code)
   else:
     print("Ответ отсутствует.")
   response = test_post_avia()
   assert response.status_code == 200   


@allure.title("Пассажир 1 взрослый+ 1 младенец")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")

def test_post_avia_3(): #Билет в 1 сторону, 1 взрослый, 1 младенец
   data = {  
    "search": {
        "id": "95c0c11c-a5f1-4ed9-8adf-0a0c9f2ebd02",
        "ticket": {
            "sort_rating": 0,
            "segments": [
                {
                    "flights": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "",
                            "equipment": "",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ],
                    "transfers": [
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": True,
                            "tags": [
                                "overnight_layover"
                            ],
                            "arrival_airport": "SVO",
                            "departure_airport": "SVO",
                            "departure_airline": "DP",
                            "arrival_airline": "DP",
                            "duration": 1960,
                            "country_code": "RU",
                            "city_code": "MOW"
                        }
                    ]
                }
            ],
            "is_direct": False,
            "max_stops": 1,
            "min_stop_duration": 1960,
            "max_stop_duration": 1960,
            "segments_time": [
                [
                    1745013000,
                    1745142000
                ]
            ],
            "segment_durations": [
                2150
            ],
            "total_duration": 2150,
            "segments_airports": [
                [
                    "CSY",
                    "KZN"
                ]
            ],
            "carriers": [
                "DP"
            ],
            "hashsum": "7170c4253b66aea7",
            "sign": "aa911b7c7e644f0dcf40d539d0eb8a34",
            "tags": [
                "has_night_transfer",
                "long_layover",
                "night_transfer",
                "overnight_layover"
            ],
            "badges": [],
            "debug": {
                "agent_id": 70,
                "popularity": 0
            },
            "extra_fares": {
                "H1|L0|CH1|R0|TBC0": [
                    {
                        "proposal_id": "70:68",
                        "index": 0
                    }
                ]
            },
            "score": 0.028988022948615834,
            "position": None,
            "segment": [
                {
                    "flight": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "",
                            "equipment": "",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ]
                }
            ],
            "terms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 8064,
                    "pricePerPerson": 4032,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 8064,
                    "searchPrice": 8064,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:68",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 8064,
                    "is_charter": False,
                    "url": "70:68"
                }
            },
            "xterms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 8064,
                    "pricePerPerson": 4032,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 8064,
                    "searchPrice": 8064,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:68",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 8064,
                    "is_charter": False,
                    "url": "70:68"
                }
            }
        },
        "search_params": {
            "precheckedFilters": {},
            "destinationCountryIata": "RU",
            "destinationCityIata": "KZN",
            "originCountryIata": "RU",
            "originCityIata": "CSY",
            "isOneWay": True,
            "isPlacesRestored": True,
            "paymentMethod": "all",
            "passengers": {
                "adults": 1,
                "children": 0,
                "infants": 1
            },
            "segments": [
                {
                    "origin": "CSY",
                    "original_origin": "CSY",
                    "origin_country": "RU",
                    "origin_type": "city",
                    "destination": "KZN",
                    "original_destination": "KZN",
                    "destination_country": "RU",
                    "destination_type": "city",
                    "date": "2025-04-18",
                    "origin_name": "Чебоксары",
                    "destination_name": "Казань",
                    "originType": "city",
                    "destinationType": "city"
                }
            ],
            "startSearch": True,
            "tripClass": "Y",
            "tripType": "oneway",
            "trip_class": "Y",
            "with_request": False,
            "originName": "Чебоксары",
            "destinationName": "Казань",
            "locale": "ru",
            "host": "search.aviasales.ru",
            "currency": "rub",
            "market": "ru",
            "formParams": {
                "passengers": {
                    "adults": 1,
                    "children": 0,
                    "infants": 1
                },
                "tripClass": "Y",
                "segments": [
                    {
                        "origin": {
                            "iata": "CSY",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "destination": {
                            "iata": "KZN",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "date": "2025-04-17T21:00:00.000Z"
                    }
                ],
                "paymentMethod": "all"
            }
        }
    }
}
   if response is not None:
     print(response.status_code)
   else:
     print("Ответ отсутствует.")
   response = test_post_avia()
   assert response.status_code == 200


#Negative
@allure.title("Билет без пассажира")
@allure.description("Поиск авиабилетов без пассажиров. Негативный.")
@allure.severity("medium")
def test_post_avia_4(): #Поиск билета без пассажира
    data = {
    "search": {
        "id": "95c0c11c-a5f1-4ed9-8adf-0a0c9f2ebd02",
        "ticket": {
            "sort_rating": 0,
            "segments": [
                {
                    "flights": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "",
                            "equipment": "",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ],
                    "transfers": [
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": True,
                            "tags": [
                                "overnight_layover"
                            ],
                            "arrival_airport": "SVO",
                            "departure_airport": "SVO",
                            "departure_airline": "DP",
                            "arrival_airline": "DP",
                            "duration": 1960,
                            "country_code": "RU",
                            "city_code": "MOW"
                        }
                    ]
                }
            ],
            "is_direct": False,
            "max_stops": 1,
            "min_stop_duration": 1960,
            "max_stop_duration": 1960,
            "segments_time": [
                [
                    1745013000,
                    1745142000
                ]
            ],
            "segment_durations": [
                2150
            ],
            "total_duration": 2150,
            "segments_airports": [
                [
                    "CSY",
                    "KZN"
                ]
            ],
            "carriers": [
                "DP"
            ],
            "hashsum": "7170c4253b66aea7",
            "sign": "aa911b7c7e644f0dcf40d539d0eb8a34",
            "tags": [
                "has_night_transfer",
                "long_layover",
                "night_transfer",
                "overnight_layover"
            ],
            "badges": [],
            "debug": {
                "agent_id": 70,
                "popularity": 0
            },
            "extra_fares": {
                "H1|L0|CH1|R0|TBC0": [
                    {
                        "proposal_id": "70:68",
                        "index": 0
                    }
                ]
            },
            "score": 0.028988022948615834,
            "position": None,
            "segment": [
                {
                    "flight": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "",
                            "equipment": "",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ]
                }
            ],
            "terms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 8064,
                    "pricePerPerson": 4032,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 8064,
                    "searchPrice": 8064,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:68",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 8064,
                    "is_charter": False,
                    "url": "70:68"
                }
            },
            "xterms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 8064,
                    "pricePerPerson": 4032,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 8064,
                    "searchPrice": 8064,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:68",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 8064,
                    "is_charter": False,
                    "url": "70:68"
                }
            }
        },
        "search_params": {
            "precheckedFilters": {},
            "destinationCountryIata": "RU",
            "destinationCityIata": "KZN",
            "originCountryIata": "RU",
            "originCityIata": "CSY",
            "isOneWay": True,
            "isPlacesRestored": True,
            "paymentMethod": "all",
            "passengers": {
                "adults": 1,
                "children": 0,
                "infants": 1
            },
            "segments": [
                {
                    "origin": "CSY",
                    "original_origin": "CSY",
                    "origin_country": "RU",
                    "origin_type": "city",
                    "destination": "KZN",
                    "original_destination": "KZN",
                    "destination_country": "RU",
                    "destination_type": "city",
                    "date": "2025-04-18",
                    "origin_name": "Чебоксары",
                    "destination_name": "Казань",
                    "originType": "city",
                    "destinationType": "city"
                }
            ],
            "startSearch": True,
            "tripClass": "Y",
            "tripType": "oneway",
            "trip_class": "Y",
            "with_request": False,
            "originName": "Чебоксары",
            "destinationName": "Казань",
            "locale": "ru",
            "host": "search.aviasales.ru",
            "currency": "rub",
            "market": "ru",
            "formParams": {
                "passengers": {
                    "adults": 0,
                    "children": 0,
                    "infants": 0
                },
                "tripClass": "Y",
                "segments": [
                    {
                        "origin": {
                            "iata": "CSY",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "destination": {
                            "iata": "KZN",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "date": "2025-04-17T21:00:00.000Z"
                    }
                ],
                "paymentMethod": "all"
            }
        }
    }
}
    if response is not None:
     print(response.status_code)
    else:
     print("Ответ отсутствует.")
    response = test_post_avia()
    assert response.status_code == 404


@allure.title("Младенцев больше чем взрослых")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону. Младенцев больше чем взрослых. Негативный")
@allure.severity("critical")
def test_post_avia_5(): #Младенцев больше чем взрослых пассажиров
    data = {
    "search": {
        "id": "95c0c11c-a5f1-4ed9-8adf-0a0c9f2ebd02",
        "ticket": {
            "sort_rating": 0,
            "segments": [
                {
                    "flights": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "",
                            "equipment": "",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ],
                    "transfers": [
                        {
                            "visa_rules": {
                                "required": False
                            },
                            "recheck_baggage": False,
                            "night_transfer": True,
                            "tags": [
                                "overnight_layover"
                            ],
                            "arrival_airport": "SVO",
                            "departure_airport": "SVO",
                            "departure_airline": "DP",
                            "arrival_airline": "DP",
                            "duration": 1960,
                            "country_code": "RU",
                            "city_code": "MOW"
                        }
                    ]
                }
            ],
            "is_direct": False,
            "max_stops": 1,
            "min_stop_duration": 1960,
            "max_stop_duration": 1960,
            "segments_time": [
                [
                    1745013000,
                    1745142000
                ]
            ],
            "segment_durations": [
                2150
            ],
            "total_duration": 2150,
            "segments_airports": [
                [
                    "CSY",
                    "KZN"
                ]
            ],
            "carriers": [
                "DP"
            ],
            "hashsum": "7170c4253b66aea7",
            "sign": "aa911b7c7e644f0dcf40d539d0eb8a34",
            "tags": [
                "has_night_transfer",
                "long_layover",
                "night_transfer",
                "overnight_layover"
            ],
            "badges": [],
            "debug": {
                "agent_id": 70,
                "popularity": 0
            },
            "extra_fares": {
                "H1|L0|CH1|R0|TBC0": [
                    {
                        "proposal_id": "70:68",
                        "index": 0
                    }
                ]
            },
            "score": 0.028988022948615834,
            "position": None,
            "segment": [
                {
                    "flight": [
                        {
                            "arrival": "SVO",
                            "arrival_date": "2025-04-18",
                            "arrival_time": "23:20",
                            "arrival_timestamp": 1745007600,
                            "departure": "CSY",
                            "departure_date": "2025-04-18",
                            "departure_time": "21:50",
                            "departure_timestamp": 1745002200,
                            "duration": 90,
                            "local_arrival_timestamp": 1745018400,
                            "local_departure_timestamp": 1745013000,
                            "number": "6816",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "",
                            "equipment": "",
                            "delay": 0,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745013000:1745018400:CSY:SVO"
                        },
                        {
                            "arrival": "KZN",
                            "arrival_date": "2025-04-20",
                            "arrival_time": "09:40",
                            "arrival_timestamp": 1745131200,
                            "departure": "SVO",
                            "departure_date": "2025-04-20",
                            "departure_time": "08:00",
                            "departure_timestamp": 1745125200,
                            "duration": 100,
                            "local_arrival_timestamp": 1745142000,
                            "local_departure_timestamp": 1745136000,
                            "number": "6841",
                            "operating_carrier": "DP",
                            "airline_id": "DP",
                            "aircraft": "Boeing 737-800 (winglets)",
                            "equipment": "73H",
                            "delay": 1960,
                            "technical_stops": [],
                            "transport": "plane",
                            "signature": "1745136000:1745142000:SVO:KZN"
                        }
                    ]
                }
            ],
            "terms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 8064,
                    "pricePerPerson": 4032,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 8064,
                    "searchPrice": 8064,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:68",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 8064,
                    "is_charter": False,
                    "url": "70:68"
                }
            },
            "xterms": {
                "70": {
                    "agentId": 70,
                    "agentLabel": "Купибилет",
                    "currency": "rub",
                    "price": 8064,
                    "pricePerPerson": 4032,
                    "cashback": 0,
                    "cashbackPerPerson": 0,
                    "unifiedPrice": 8064,
                    "searchPrice": 8064,
                    "worstBags": {
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        }
                    },
                    "weight": 0.02990978363247634,
                    "tags": [
                        "cheap",
                        "virtual_interline_domestic",
                        "with_cache"
                    ],
                    "id": "70:68",
                    "flightTerms": [
                        [
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6816"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            },
                            {
                                "fareCode": "QECONALL",
                                "tripClass": "Y",
                                "marketingCarrierDesignator": {
                                    "carrier": "DP",
                                    "airlineId": "DP",
                                    "number": "6841"
                                },
                                "baggage": {
                                    "count": 0
                                },
                                "handbags": {
                                    "count": 1,
                                    "weight": 10,
                                    "dimensions": "36x30x27"
                                },
                                "isCharter": False,
                                "seatsAvailable": 9,
                                "additionalTariffInfo": {
                                    "changeAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "changeBeforeFlight": {
                                        "available": True
                                    },
                                    "returnAfterFlight": {
                                        "available": False,
                                        "isFromConfig": True
                                    },
                                    "returnBeforeFlight": {
                                        "available": False
                                    }
                                },
                                "mergedTermsInfo": {
                                    "baggage": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "handbags": {
                                        "isFromConfig": {
                                            "count": True,
                                            "weight": True,
                                            "dimensions": "TruexTruexTrue"
                                        },
                                        "mismatch": {}
                                    },
                                    "changeAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "changeBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "returnAfterFlight": {
                                        "isFromConfig": {
                                            "available": True,
                                            "penaltyCurrencyCode": True,
                                            "penaltyValue": True
                                        },
                                        "mismatch": {}
                                    },
                                    "returnBeforeFlight": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtPurchase": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    },
                                    "seatAtRegistration": {
                                        "isFromConfig": {},
                                        "mismatch": {}
                                    }
                                }
                            }
                        ]
                    ],
                    "transferTerms": [
                        [
                            {
                                "isVirtualInterline": True,
                                "tags": [
                                    "virtual_interline_domestic"
                                ]
                            }
                        ]
                    ],
                    "assisted": False,
                    "seatsAvailable": 9,
                    "badPartner": False,
                    "fromMainAirline": False,
                    "debugInfo": None,
                    "minimumFare": {
                        "code": "",
                        "baggage": {
                            "count": 0
                        },
                        "handbags": {
                            "count": 1,
                            "weight": 10,
                            "dimensions": "36x30x27"
                        },
                        "changeBeforeFlight": {
                            "available": True
                        },
                        "changeAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        },
                        "returnBeforeFlight": {
                            "available": False
                        },
                        "returnAfterFlight": {
                            "available": False,
                            "is_from_config": True
                        }
                    },
                    "gate_id": 70,
                    "unified_price": 8064,
                    "is_charter": False,
                    "url": "70:68"
                }
            }
        },
        "search_params": {
            "precheckedFilters": {},
            "destinationCountryIata": "RU",
            "destinationCityIata": "KZN",
            "originCountryIata": "RU",
            "originCityIata": "CSY",
            "isOneWay": True,
            "isPlacesRestored": True,
            "paymentMethod": "all",
            "passengers": {
                "adults": 1,
                "children": 0,
                "infants": 1
            },
            "segments": [
                {
                    "origin": "CSY",
                    "original_origin": "CSY",
                    "origin_country": "RU",
                    "origin_type": "city",
                    "destination": "KZN",
                    "original_destination": "KZN",
                    "destination_country": "RU",
                    "destination_type": "city",
                    "date": "2025-04-18",
                    "origin_name": "Чебоксары",
                    "destination_name": "Казань",
                    "originType": "city",
                    "destinationType": "city"
                }
            ],
            "startSearch": True,
            "tripClass": "Y",
            "tripType": "oneway",
            "trip_class": "Y",
            "with_request": False,
            "originName": "Чебоксары",
            "destinationName": "Казань",
            "locale": "ru",
            "host": "search.aviasales.ru",
            "currency": "rub",
            "market": "ru",
            "formParams": {
                "passengers": {
                    "adults": 1,
                    "children": 0,
                    "infants": 5
                },
                "tripClass": "Y",
                "segments": [
                    {
                        "origin": {
                            "iata": "CSY",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "destination": {
                            "iata": "KZN",
                            "type": "city",
                            "isVirtual": True,
                            "name": ""
                        },
                        "date": "2025-04-17T21:00:00.000Z"
                    }
                ],
                "paymentMethod": "all"
            }
        }
    }
}
    if response is not None:
     print(response.status_code)
    else:
     print("Ответ отсутствует.")
    response = test_post_avia_5()
    assert response.status_code == 200
