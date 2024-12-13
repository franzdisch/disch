import azure.functions as func
import logging
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP request received for squaring a number.")

    try:
        # Zahl aus dem Query-Parameter holen
        number = req.params.get("number")

        # Wenn die Zahl nicht im Query ist, aus dem Body holen
        if not number:
            try:
                req_body = req.get_json()
                number = req_body.get("number")
            except ValueError:
                pass

        # Prüfen, ob die Eingabe vorhanden ist und eine Zahl ist
        if number is None or not number.isdigit():
            return func.HttpResponse(
                "Please provide a valid number as a query parameter or in the request body.",
                status_code=400
            )

        # Quadrat berechnen
        number = int(number)
        result = number ** 2

        # JSON-Antwort erstellen
        response = {"input": number, "result": result}

        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return func.HttpResponse(
            f"Internal Server Error: {str(e)}",
            status_code=500
        )
