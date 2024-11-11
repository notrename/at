import json


class JsonWriter:

    @staticmethod
    def write_to_file(fn):
        def wrapper(*args, **kwargs):
            filename = 'pets.json'
            result = fn(*args, **kwargs)
            with open(filename, 'r', encoding='utf8') as f:
                data = f.read()
                if data:
                    pets = json.loads(data)
                else:
                    pets = []
            if 'data' in result:
                with open(filename, 'w', encoding='utf8') as f:
                    pets.append(result.get('data'))
                    f.write(json.dumps(pets, ensure_ascii=False, indent=2))
            if 'id' in result or 'name' in result:
                with open(filename, 'w', encoding='utf8') as f:
                    pets.append(result)
                    f.write(json.dumps(pets, ensure_ascii=False, indent=2))
            return result
        return wrapper


class StatusChecker:
    @staticmethod
    def success_check(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            if isinstance(result, int):
                print(f'status code: {result}')
            if 'status_code' in result:
                print(f'status code: {result.get("status_code")}')
            return result
        return wrapper
