def get_hash(password: str) -> str:
        from hashlib import md5
        baite_str: str = password.encode('utf-8')
        hash_object: str = md5(baite_str)
        return hash_object.hexdigest()