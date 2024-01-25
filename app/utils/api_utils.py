class ApiResponse:
    @staticmethod
    def success(data):
        return data

    @staticmethod
    def error(message):
        return {"success": False, "error": message}