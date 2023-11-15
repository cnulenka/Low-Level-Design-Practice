package org.cache.eviction;

import java.util.LinkedHashMap;
import java.util.Map;

public class LRUEvictionPolicy<Key> implements EvictionPolicy<Key> {

    LinkedHashMap<Key, Key> linkedHashMap;

    public LRUEvictionPolicy() {
        linkedHashMap = new LinkedHashMap<>();
    }

    @Override
    public Key evict() {
        Key key = null;

        for (Map.Entry<Key, Key> mapElement : linkedHashMap.entrySet()) {
            key = mapElement.getKey();
            break;
        }

        if(key != null){
            linkedHashMap.remove(key);
        }
        return key;
    }

    @Override
    public void keyAccessed(Key key) {
        linkedHashMap.remove(key);
        linkedHashMap.put(key, key);
    }
}
