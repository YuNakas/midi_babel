from module.ui.pages import top, midi, select_midi_track, key_mapping_from, key_mapping_to,\
    create_key_mapping, edit_key_mapping, generate_converter, convert_end, file_output, midi_file_output,\
    appendix
from gv import g

def create_view(page):
    def route_change(e):
        page.views.clear()
        page.views.append(
            top.top_view(page.go)
        )
        if page.route == "/midi":
            page.views.append(
                midi.midi_view(page, page.go, return_top)
            )
        if page.route == "/select_midi_track":
            page.views.append(
                select_midi_track.select_midi_track_view(page.go)
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
                convert_end.convert_end_view(page, return_top)
            )
        if page.route == "/file_output":
            page.views.append(
                file_output.file_output_view(page, page.go, return_top)
            )
        if page.route == "/midi_file_output":
            page.views.append(
                midi_file_output.midi_file_output_view(page, return_top)
            )
        if page.route == "/appendix":
            page.views.append(
                appendix.appendix_view(page.go)
            )
        page.update()
    
    def return_top(e):
        """state情報を初期化してtopに戻る"""
        g.reset_class()
        page.go("/")
        
    page.on_route_change = route_change
    page.on_view_pop = return_top

    page.go(page.route)
