 #include <stdio.h>
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
#include <raylib.h>

int main(void) {
    // 1. Initialize Lua State
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);

    // 2. Load Lua script
    if (luaL_dofile(L, "config.lua") != LUA_OK) {
        fprintf(stderr, "Error loading Lua script: %s\n", lua_tostring(L, -1));
        lua_close(L);
        return 1;
    }

    // 3. Read global variables from Lua
    lua_getglobal(L, "window_width");
    int width = (int)lua_tonumber(L, -1);
    lua_pop(L, 1);

    lua_getglobal(L, "window_height");
    int height = (int)lua_tonumber(L, -1);
    lua_pop(L, 1);

    lua_getglobal(L, "window_title");
    const char *title = lua_tostring(L, -1);
    lua_pop(L, 1);

    // 4. Initialize Raylib Window
    InitWindow(width, height, title);
    SetTargetFPS(60);

    // 5. Main Loop
    while (!WindowShouldClose()) {
        // Optional: Call a Lua function here to update logic each frame
        
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Read dynamic shape position from Lua table
        lua_getglobal(L, "shape");
        
        lua_getfield(L, -1, "x");
        float x = (float)lua_tonumber(L, -1);
        lua_pop(L, 1);

        lua_getfield(L, -1, "y");
        float y = (float)lua_tonumber(L, -1);
        lua_pop(L, 1);

        lua_getfield(L, -1, "size");
        float size = (float)lua_tonumber(L, -1);
        lua_pop(L, 2); // pop size and shape table

        // Render using C (Raylib)
        DrawRectangle((int)x - size/2, (int)y - size/2, (size_t)size, (size_t)size, BLUE);
        DrawText("C handles rendering, Lua handles data/logic.", 10, 10, 20, DARKGRAY);

        EndDrawing();
    }

    // 6. Cleanup
    CloseWindow();
    lua_close(L);
    return 0;
}
