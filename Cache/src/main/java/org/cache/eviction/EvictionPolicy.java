package org.cache.eviction;

public interface EvictionPolicy<Key> {
    public Key evict();
    public void keyAccessed(Key key);
}
