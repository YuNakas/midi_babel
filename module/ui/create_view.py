from module import _init
from module.ui.pages import top, midi, select_midi_track, map, key_mapping_from, key_mapping_to, create_key_mapping, edit_key_mapping, generate_converter, convert_end

def create_view(page):
    def route_change(e):
        page.views.clear()
        page.views.append(
            top.top_view(page.go)
        )
        if page.route == "/midi":
            page.views.append(
                midi.midi_view(page.go)
            )
        if page.route == "/select_midi_track":
            page.views.append(
                select_midi_track.select_midi_track_view(page.go)
            )
        if page.route == "/map":
            page.views.append(
                map.map_view(page.go)
            )
        if page.route == "/key_mapping_from":
            page.views.append(
                key_mapping_from.key_mapping_from_view(page.go)
            )
        if page.route == "/key_mapping_to":
            page.views.append(
                key_mapping_to.key_mapping_to_view(page.go)
            )
        if page.route == "/create_key_mapping":
            page.views.append(
                create_key_mapping.create_key_mapping_view(page.go)
            )
        if page.route == "/edit_key_mapping":
            page.views.append(
                edit_key_mapping.edit_key_mapping_view(page.go)
            )
        if page.route == "/generate_converter":
            page.views.append(
                generate_converter.generate_converter_view(page.go)
            )
        if page.route == "/convert_end":
            page.views.append(
                convert_end.convert_end_view(return_top)
            )
        page.update()
    
    def return_top(e):
        # コンフィグ情報を再取得
        _init.init_config()

        # 選択した情報などを初期化
        _init.init_state()

        # midiファイルの情報を初期化
        _init.init_midi()

        page.go("/")
        
    page.on_route_change = route_change
    page.on_view_pop = return_top

    page.go(page.route)
