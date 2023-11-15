package org.cache.storage;

import org.cache.exceptions.KeyNotFoundException;
import org.cache.exceptions.StorageFullException;

import java.util.HashMap;
import java.util.Map;

public class HashMapStorage<Key, Value> implements Storage<Key, Value> {
    Map<Key, Value> hashMap;
    Integer capacity;

    public HashMapStorage(Integer capacity){
        hashMap = new HashMap<>();
        this.capacity = capacity;
    }

    @Override
    public Value get(Key key) throws KeyNotFoundException {
        if(!hashMap.containsKey(key)){
            throw new KeyNotFoundException();
        }
        return hashMap.get(key);
    }

    @Override
    public void remove(Key key) throws KeyNotFoundException {
        if(!hashMap.containsKey(key)) { // Improvement: remove also needs key check
            throw new KeyNotFoundException();
        }
        hashMap.remove(key);
    }

    @Override
    public void put(Key key, Value value) throws StorageFullException {
        if(isStorageFull()) {
            throw new StorageFullException();
        }
        hashMap.put(key, value);
    }

    private boolean isStorageFull() {
        // Improvement: separate method
        return hashMap.size() == capacity;
    }
}
